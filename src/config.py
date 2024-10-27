import json
import os

def read_config():
    if not os.path.exists("./conf/config.json"):
        return create_default_config()
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
    with open('./safe/config.json', 'w', encoding='utf-8') as f:
        json.dump(default_config, f, ensure_ascii=False, indent=4)
    return default_config
