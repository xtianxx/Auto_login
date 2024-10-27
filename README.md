# Auto_login

## 简介
Auto_login 是一个自动登录校园网的项目，旨在简化用户的登录流程，方便学生和教职工快速连接到校园网络。
通过wireshark抓包，分析校园网的登录流程，使用Python编写脚本实现自动登录。
代码主要由ai编写。

## 安装

1. 克隆项目：
   ```bash
   git clone https://github.com/xtianxx/Auto_login.git
2. 安装依赖：
    ```bash
   pip install -r requirements.txt

## 使用
1. 运行项目：
    ```bash
   python main.py

2. 初次运行会在conf目录下生成配置文件。
3. 在配置文件中 config.json 填写校园网的用户名和密码。
4. 之后运行 1 ，会自动尝试登录校园网。
 注意事项:
1. 本项目仅适用于校园网登录，其他网络环境下可能无法正常使用。
2. 本项目仅供学习和研究使用，请勿用于非法用途。

## 参考

思路来源：https://github.com/wnzzer/wifi-auto-connect