# _*_coding:utf-8_*_
# Author   : Leo
# Time     : 19/12/2018
import requests

response = requests.get("https://www.baidu.com/img/bd_logo1.png")
with open("a.png","wb") as f:
    f.write(response.content)