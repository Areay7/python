import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm


class CoronaVirusSpider(object):

    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_content_from_url(self, url):
        """
        根据url, 获取响应内容的字符串数据
        :param url: 请求的URL
        :return: 响应内容的自促穿
        """
        response = requests.get(url)
        return response.content.decode()

    def parse_home_page(self, home_page, tag_id):
        """
        解析首页内容,获取解析后的Python数据
        :param home_page: 首页的内容
        :return: 解析后的Python数据
        """
        # 2.从疫情首页,提取最近一日各国疫情数据
        soup = BeautifulSoup(home_page, 'html.parser')
        script = soup.find(id=tag_id)
        text = script.text
        # print(text)

        # 3.从疫情数据中,获取json格式的字符串
        json_str = re.findall(r'\[.+\]', text)[0]
        # print(json_str)

        # 4.把json格式的字符串转换成Python类型
        data = json.loads(json_str)
        return data

    def parse_corona_virus(self, last_day_cornoa_virus_of_china, desc):
        # 定义列表, 用于存储各国从9月1日以来的疫情数据
        corona_virus = []
        # 2. 遍历各国疫情数据, 获取统计的URL
        for country in tqdm(last_day_cornoa_virus_of_china, desc):

            # 3. 发送请求, 获取各省疫情json字符串
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            # print(statistics_data_json_str)

            # 4.  # 解析各省疫情json字符串, 并添加到列表中
            statistics_data = json.loads(statistics_data_json_str)['data']
            # print(statistics_data)
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']
                if country.get('countryShortCode'):
                    one_day['countryShortCode'] = country['countryShortCode']
            # print(statistics_data)
            corona_virus.extend(statistics_data)
            # print(corona_virus)
        return corona_virus

    def load(self, path):
        """
        根据路径, 加载数据
        :param path:
        :return:
        """
        with open(path, encoding='utf-8') as fp:
            data = json.load(fp)
        return data

    def save(self, data, path):
        # 5.把json格式保存,最近一日各国疫情数据
        with open(path, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False)

    def crawl_last_day_corona_virus(self):
        """
        采集最近一天的各国疫情数据
        :return:
        """
        # 1. 发送请求,获取首页内容
        home_page = self.get_content_from_url(self.home_url)
        # 2. 解析首页内容获取最近一天的各国疫情数据
        last_day_corona_virus = self.parse_home_page(home_page, tag_id='getListByCountryTypeService2true')
        # 3. 保存数据
        self.save(last_day_corona_virus, '../data/last_day_corona_virus.json')

    def crawl_corona_virus(self):
        """
        采集从9月1日以来各国疫情数据
        :return:
        """
        # 1. 加载各国疫情数据
        last_day_corona_virus = self.load('../data/last_day_corona_virus.json')
        # print(last_day_corona_virus)

        # 定义列表, 用于存储各国从9月1日以来的疫情数据
        corona_virus = self.parse_corona_virus(last_day_corona_virus, desc='采集9月1日以来的各国疫情信息')

            # 5. 把列表以json格式保存为文件
        self.save(corona_virus,'../data/corona_virus.json')

    def crawl_last_day_cornoa_virus_of_china(self):
        """
        采集最近一日各省疫情数据
        :return:
        """
        # 1. 发送请求，获取疫情首页
        home_page = self.get_content_from_url(self.home_url)
        # 2. 解析疫情首页, 获取最近一日各省份疫情数据
        last_day_cornoa_virus_of_china = self.parse_home_page(home_page,tag_id='getAreaStat')

        # 3. 保存疫情数据
        self.save(last_day_cornoa_virus_of_china,"../data/last_day_cornoa_virus_of_china.json")


    def crawl_cornoa_virus_of_china(self):
        """
        采集从9月1日以来的全国个省份的疫情数据
        :return:
        """
        # 加载最近一日全国疫情数据
        last_day_cornoa_virus_of_china = self.load('../data/last_day_cornoa_virus_of_china.json')

        # 遍历最近一日全国疫情数据, 获取各省疫情数据URL
        corona_virus = self.parse_corona_virus(last_day_cornoa_virus_of_china, '采集9月1日以来的各省份疫情信息')

        # 以json格式保存疫情信息
        self.save(corona_virus,'../data/cornoa_virus_of_china.json')



    def run(self):
        # self.crawl_last_day_corona_virus()
        self.crawl_corona_virus()
        # self.crawl_last_day_cornoa_virus_of_china()
        self.crawl_cornoa_virus_of_china()

if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()