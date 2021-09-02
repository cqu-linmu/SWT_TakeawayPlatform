import zlib


def compress(str1):
    return zlib.compress(str1.encode("utf-8")).decode("utf-8")


def decompress(strFlow2):
    """
    解压缩字符串
    :param strFlow2:
    :return:
    """
    return zlib.decompress(strFlow2.encode("utf-8")).decode("utf-8")
