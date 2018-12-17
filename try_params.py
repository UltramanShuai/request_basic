# _*_coding:utf-8_*_
# Author   : Leo
# Time     : 17/12/2018
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
param={"wd":"python"}
url_temp="https://www.baidu.com/s"

response=requests.get(url_temp,headers=headers,params=param)
print(response.status_code)
print(response.request.url)