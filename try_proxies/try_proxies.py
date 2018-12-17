# _*_coding:utf-8_*_
# Author   : Leo
# Time     : 18/12/2018

import requests


class TryProxies:

    def __init__(self, url):
        self.proxies = {"http": "http://101.89.132.131:80"}
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
        self.url = url

    def parse_url(self):
        response = requests.get(url=self.url, headers=self.headers, proxies=self.proxies)
        print(response.status_code)

    def run(self):
        self.parse_url()


if __name__ == '__main__':
    try_proxies = TryProxies("http://www.baidu.com")
    try_proxies.run()
