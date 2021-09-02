# encoding:utf-8
__author__ = 'James Lau'

import hashlib
import re


def __original_shorturl(url):
    '''
  算法：
  ① 将长网址用md5算法生成32位签名串，分为4段,，每段8个字符；
  ② 对这4段循环处理，取每段的8个字符, 将他看成16进制字符串与0x3fffffff(30位1)的位与操作，超过30位的忽略处理；
  ③ 将每段得到的这30位又分成6段，每5位的数字作为字母表的索引取得特定字符，依次进行获得6位字符串；
  ④ 这样一个md5字符串可以获得4个6位串，取里面的任意一个就可作为这个长url的短url地址。
  （出现重复的几率大约是n/(32^6) 也就是n/1,073,741,824，其中n是数据库中记录的条数）
  '''
    base32 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
              'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
              'y', 'z',
              '0', '1', '2', '3', '4', '5'
              ]
    m = hashlib.md5()
    m.update(url)
    hexStr = m.hexdigest()
    hexStrLen = len(hexStr)
    subHexLen = hexStrLen // 8
    output = []
    for i in range(0, subHexLen):
        subHex = '0x' + hexStr[i * 8:(i + 1) * 8]
        res = 0x3FFFFFFF & int(subHex, 16)
        out = ''
        for j in range(6):
            val = 0x0000001F & res
            out += (base32[val])
            res = res >> 5
        output.append(out)
    return output


def shorturl(url):
    """
      算法：
      ①从原始url中提取域名，提取数字（最多后6位）；
      ②将所得的数字与4取模，根据所得的余数决定从第一步算法中得到的4个shorturl中选取哪一个；
      ③从域名中提取特征串：一级域名中的第一个字符和后面二个辅音（如果辅音不足2个取任意前两个）；
      ④域名特征串和选定的shorturl拼接成9位字符为最终的shorturl；
      （后两个步骤是将冲突控制在一个domain内）
    """
    match_full_domain_regex = re.compile(
        u'^https?:\/\/(([a-zA-Z0-9_\-\.]+[a-zA-Z0-9_\-]+\.[a-zA-Z]+)|([a-zA-Z0-9_\-]+\.[a-zA-Z]+)).*$')
    match_full_domain = match_full_domain_regex.match(url)
    if match_full_domain is not None:
        full_domain = match_full_domain.group(1)
    else:
        return None
    not_numeric_regex = re.compile(u'[^\d]+')
    numeric_string = not_numeric_regex.sub(r'', url)
    if numeric_string is None or numeric_string == '':
        numeric_string = '0'
    else:
        numeric_string = numeric_string[-6:]
    domainArr = full_domain.split('.')
    domain = domainArr[1] if len(domainArr) == 3 else domainArr[0]
    vowels = 'aeiou0-9'
    if len(domain) <= 3:
        prefix = domain
    else:
        prefix = re.compile(u'[%s]+' % vowels).sub(r'', domain[1:])
        prefix = '%s%s' % (domain[0], prefix[:2]) if len(prefix) >= 2 else domain[0:3]
    t_shorturl = __original_shorturl(url)
    t_choose = int(numeric_string) % 4
    result = '%s%s' % (prefix, t_shorturl[t_choose])
    return result
