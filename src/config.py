import json
import os
from tkinter import messagebox


def read_config():
    if not os.path.exists("./conf/config.json"):
        messagebox.showwarning("警告", "配置文件不存在，已创建默认配置文件。请到目录下的 conf/config.json 中配置你的账号密码。"
                                      "之后请重新运行本程序。")
        create_default_config()
        exit(0)
    with open('./conf/config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config

def create_default_config():
    os.makedirs('./conf', exist_ok=True)
    default_config = {
        "comments": {
            "userid": "学号+@xxxy+运营商缩写",
            "运营商": "dx yd ld"
        },
        "UserInfo": {
            "userid": "youruserid",
            "passwd": "your_passwd",
            "wlanacname": "XXXY-New-BRAS"
        }
    }
    with open('./conf/config.json', 'w', encoding='utf-8') as f:
        json.dump(default_config, f, ensure_ascii=False, indent=4)
    return default_config
