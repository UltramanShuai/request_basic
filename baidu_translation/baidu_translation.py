# _*_coding:utf-8_*_
# Author   : Leo
# Time     : 17/12/2018
import requests
import json
import sys


class Translation:

    def __init__(self, query):
        # set the translation page
        self.post_url = "https://fanyi.baidu.com/basetrans"
        # simulate a mobile user
        self.header = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        # get the query
        self.query_string = query

    def get_language(self):
        # get the type of query language from url
        language_return = requests.post(url="https://fanyi.baidu.com/langdetect", data={"query": self.query_string},
                                        headers=self.header).content.decode()
        query_language = json.loads(language_return)["lan"]
        # calculate the result language
        result_language = "zh" if query_language == "en" else "en"
        # return the tupe of language type
        return query_language, result_language

    def init_data(self, laguage):
        # initial the data post to the url based on query, language type of query and language type of result
        return {
            'from': laguage[0],
            'to': laguage[1],
            "query": self.query_string,
        }

    def parse_url(self, data, header):
        # get the translation result from url
        response = requests.post(url=self.post_url, data=data, headers=header)
        dict_return = json.loads(response.content.decode())
        result_return = dict_return["trans"][0]["dst"]
        print("The result:", result_return)

    def run(self):
        self.parse_url(self.init_data(self.get_language()), self.header)


if __name__ == '__main__':
    # get the input query from args
    try:
        translate = Translation(sys.argv[1])
        translate.run()
    except IndexError:
        print("Please input a query after .py file")
        print("etc. python baidu_translation.py 'How are you'")
