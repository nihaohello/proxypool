# coding=utf-8
import requests
import re
import hackhttp
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import random
class Tutu_Ip_Proxy(object):
    def __init__(self):
        self.ua=UserAgent()
    def run(self):
        self.xicidaili()
        self.kuaidaili()
        self.iphai()
        self.yundaili()
    def get_ip66__proxy_ips(self):
        pass
    def xicidaili(self):
        url = 'http://www.xicidaili.com/'
        time.sleep(random.randint(6, 8))
        headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        request = requests.get(url, headers=headers)
        response = request.text
        bsObj = BeautifulSoup(response, 'lxml')  # 解析获取到的html
        ip_text = bsObj.findAll('tr', {'class': 'odd'})  # 获取带有IP地址的表格的所有行
        ip_list = []
        for i in range(len(ip_text)):
            ip_tag = ip_text[i].findAll('td')
            ip_port = ip_tag[1].get_text() + ':' + ip_tag[2].get_text()  # 提取出IP地址和端口号
            ip_list.append(ip_port)
        # print("共收集到了{}个代理IP".format(len(ip_list)))
        # print(ip_list)
        self.fave_ips(ip_list)
        # return ip_list

    def kuaidaili(self):
        url = 'https://www.kuaidaili.com/free/inha/'
        url2='https://www.kuaidaili.com/free/intr/'
        url_list = [url + str(i + 1) for i in range(5)]  # 生成url列表，5代表只爬取5页
        url_list2 = [url + str(i + 1) for i in range(5)]  # 生成url列表，5代表只爬取5页
        ip_list = []
        for i in range(len(url_list)):
            url = url_list[i]
            time.sleep(random.randint(6, 8))
            html = requests.get(url=url, ).text
            regip = '<td.*?>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>.*?<td.*?>(\d{1,5})</td>'
            matcher = re.compile(regip, re.S)
            ipstr = re.findall(matcher, html)
            time.sleep(1)
            for j in ipstr:
                ip_list.append(j[0] + ':' + j[1])  # ip+port
        for i in range(len(url_list2)):
            url = url_list2[i]
            time.sleep(random.randint(6, 8))
            html = requests.get(url=url, ).text
            regip = '<td.*?>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>.*?<td.*?>(\d{1,5})</td>'
            matcher = re.compile(regip, re.S)
            ipstr = re.findall(matcher, html)
            time.sleep(1)
            for j in ipstr:
                ip_list.append(j[0] + ':' + j[1])  # ip+port
        # return ip_list
        self.fave_ips(ip_list)
    def yundaili(self):
        """
        云代理 http://www.ip3366.net/free/
        :return:
        """
        urls = ['http://www.ip3366.net/free/','http://www.ip3366.net/free/?stype=1&page=2',\
                'http://www.ip3366.net/free/?stype=1&page=3','http://www.ip3366.net/free/?stype=1&page=4',\
                'http://www.ip3366.net/free/?stype=1&page=5','http://www.ip3366.net/free/?stype=1&page=6',\
                'http://www.ip3366.net/free/?stype=1&page=7',\
                'http://www.ip3366.net/free/?stype=2','http://www.ip3366.net/free/?stype=2&page=2',\
                'http://www.ip3366.net/free/?stype=2&page=3','http://www.ip3366.net/free/?stype=2&page=4',\
                'http://www.ip3366.net/free/?stype=2&page=5','http://www.ip3366.net/free/?stype=2&page=6',\
                'http://www.ip3366.net/free/?stype=2&page=7']
        ips_list=[]
        for url in urls:
            time.sleep(random.randint(6, 8))
            r = requests.get(url, timeout=10)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            for proxy in proxies:
                proxy = str(proxy)
                proxy = proxy.replace("'", "").replace(" ", "").replace("(", "").replace(")", "").replace(",", ":")
                ips_list.append(proxy)
                # ('112.85.166.119', '9999')
                # print(proxy)
        self.fave_ips(ips_list)
    def iphai(self):
        """
        IP海 http://www.iphai.com/free/ng
        :return:
        """
        urls = [
            'http://www.iphai.com/free/ng',
            'http://www.iphai.com/free/np',
            'http://www.iphai.com/free/wg',
            'http://www.iphai.com/free/wp'
        ]
        ips_list=[]
        for url in urls:
            time.sleep(random.randint(6,8))
            r = requests.get(url, timeout=10)
            proxies = re.findall(r'<td>\s*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*?</td>[\s\S]*?<td>\s*?(\d+)\s*?</td>',r.text)
            for proxy in proxies:
                # ('217.182.249.105', '80')
                proxy=str(proxy)
                proxy=proxy.replace("'","").replace(" ","").replace("(","").replace(")","").replace(",",":")
                ips_list.append(proxy)
                # print(proxy)
        self.fave_ips(ips_list)
    def fave_ips(self,new_ips):
        temp_ips = []
        for i in new_ips:
            i = i.replace("u", "")
            temp_ips.append(i)
        new_ips = temp_ips
        # 获得all_ips.txt的所有ip
        f = open("/home/www/htdocs/all_ips.txt")
        all_ips = set()
        for i in f.readlines():
            all_ips.add(i.rstrip("\n"))
        f.close()
        # 将获取的new_ips存入总all_ips,方便以后统计哪些代理ip稳定
        with open("/home/www/htdocs/all_ips.txt", "a+") as f:
            for ip in new_ips:
                if ip not in all_ips:
                    f.write(str(ip))
                    f.write("\n")
        f.close()
        # 与old_ip比较,更新ip66的ip内容
        old_check_ips=[]
        f=open("/home/www/htdocs/check_ips.txt")
        for i in f.readlines():
            old_check_ips.append(i.rstrip("\n"))
        f.close()
        with open("/home/www/htdocs/check_ips.txt", "a+") as f:
            for ip in new_ips:
                if ip not in old_check_ips:
                    f.write(str(ip))
                    f.write("\n")
        f.close()

Tutu_Ip_Proxy().run()