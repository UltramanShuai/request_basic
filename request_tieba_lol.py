# _*_coding:utf-8_*_
# Author   : Leo
# Time     : 17/12/2018
import os
import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
        pass

    def get_url_list(self):
        return [self.url.format(i * 50) for i in range(1000)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url=url, headers=self.header)
        return response.content.decode()

    def save_html(self, str_url, page_num):

        folder_path = "./" + self.tieba_name
        file_path = str(folder_path + "/page-{}.html").format(page_num)

        folder = os.path.exists(folder_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(folder_path)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str_url)

    def run(self):

        url_list = self.get_url_list()
        for url in url_list:
            page_num = url_list.index(url) + 1
            str_url = self.parse_url(url)
            self.save_html(str_url, page_num)


if __name__ == '__main__':
    tieba_spider = TiebaSpider("lol")
    tieba_spider.run()
