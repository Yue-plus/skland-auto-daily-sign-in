# 森空岛自动每日签到

## 配置

### 安装依赖

`requests` 库用于发送网络请求，参考：
[官方文档](https://requests.readthedocs.io/en/latest/)
| [中文文档](https://requests.readthedocs.io/projects/cn/zh_CN/latest/)

```shell
pip install requests
```

### 配置 `CRED` 与 `COOKIE`

打开 APP 的签到页面时可通过抓包工具抓取 `https://zonai.skland.com/api/v1/game/attendance` 请求头中的 `cred` 和 `cookie` 值；
编辑 `main.py` 中 `CRED` 与 `COOKIE` 的值。

## 运行

```shell
python3 ./main.py
```
