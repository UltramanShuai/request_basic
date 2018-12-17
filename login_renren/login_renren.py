# _*_coding:utf-8_*_
# Author   : Leo
# Time     : 18/12/2018
import sys

import requests


class LoginRenren:
    def __init__(self, account, password):
        self.post_url = "http://www.renren.com/PLogin.do"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
        self.post_data = {"email": account,
                          "password": password}

    def get_session(self):
        session = requests.session()
        session.post(self.post_url, data=self.post_data, headers=self.header)
        response = session.get("http://www.renren.com/316229288/profile", headers=self.header)
        return response

    def save_page(self, response):
        with open("renren.html", "w", encoding="utf-8") as f:
            f.write(response.content.decode())

    def run(self):
        self.save_page(self.get_session())


if __name__ == '__main__':
    try:
        login_renren = LoginRenren(sys.argv[1], sys.argv[2])
        login_renren.run()
    except IndexError:
        print("Please input account and password after .py file")
        print("etc. python login_renren.py ThisIsAnAccount ThisIsAPassword")
        