import json

import requests
import socket
from config import read_config

def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception as e:
        return None

def login():
    login_url = "http://172.25.100.210:6060/quickauth.do"
    wlanuserip = get_local_ip()

    config = read_config()

    params = {
        'userid': config["UserInfo"]["userid"],
        'passwd': config["UserInfo"]["passwd"],
        'wlanuserip': wlanuserip,
        'wlanacname': config["UserInfo"]["wlanacname"],
    }

    try:
        response = requests.get(login_url, params=params)
        response.raise_for_status()
        response_data = response.json()
        return response_data, wlanuserip
    except requests.RequestException as e:
        return None, str(e)
    except json.JSONDecodeError:
        return None, "解析响应数据时出错"
