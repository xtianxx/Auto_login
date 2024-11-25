import requests
import time

def test_network():
    while True:
        try:
            response = requests.get("http://www.msftconnecttest.com/", timeout=5)
            if response.status_code == 200:
                break
        except requests.RequestException:
            time.sleep(2)
