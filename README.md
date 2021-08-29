# 食为天外卖平台 (SWT_TakeawayPlatform)

> 基于 Python web 框架的订餐外卖系统

## 项目介绍

本项目是一个互联网创新型综合性项目，通过对市场上主流订餐外卖网站（“饿了么”）的分析和调查，整理需求，定位目标人群，找准赢利点，逆向仿制订餐外卖系统。

## 项目内容

- 市场分析，需求分析，目标定位
- 系统设计、UI 设计
- 前后台交互、数据传输、服务器数据处理、客户端数据处理、数据存储
- 基于大数据的用户画像
- 基于地理位置的餐馆推荐
- 基于用户喜好的热门餐馆和美食推荐算法等。

文档编辑地址：
【接口文档】https://mubu.com/colla/7a0ZPCrMGI6

【项目结构】https://mubu.com/colla/75rMEBe2Kl6

运行注意事项：

- 前端项目部署时，由于 vite 模块的一些 bug , 导致从属于 vite 框架下的一些 esbuild 内嵌模块没有正确安装。

  请在 npm i 后使用 node .\node_modules\vite-plugin-mock\node_modules\esbuild\install.js 来配置前端环境以保证 npm run dev 能正常运行。
