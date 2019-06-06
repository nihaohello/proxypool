#coding=utf-8
import requests
import time
import random
class check_ip_proxy(object):
    def __init__(self):
        pass
    def run(self):
        f = open("/home/www/htdocs/all_ips.txt")
        old_ips = []
        for i in f.readlines():
            old_ips.append(i.rstrip("\n"))
        f.close()
        # print(old_ips)
        self.check_ip(old_ips)
    def check_ip(self,ips):
        live_ips=[]
        for ip in ips:
            try:
                s = requests.get('http://www.baidu.com/', proxies={"https": "https://" + str(ip)}, timeout=2)
                if s.status_code == 200:
                    print("成功" + ":" + (str("https://" + ip)))
                    # self.file_save(str("https://" + ip))
                    live_ips.append(str("https://" + ip))
            except Exception as e:
                pass
            try:
                s = requests.get('https://www.baidu.com/', proxies={"http": "http://" + str(ip)}, timeout=2)
                if s.status_code == 200:
                    print("成功" + ":" + (str("http://" + ip)))
                    # self.file_save(str("http://" + ip))
                    live_ips.append(str("http://" + ip))
            except Exception as e:
                pass
    # def file_save(self,ip):
        old_ips_proxies = []
        f = open("/home/www/htdocs/ips_proxies.txt")
        for i in f.readlines():
            old_ips_proxies.append(i.rstrip("\n"))
        f.close()
        # 老的代理ips+新检测出来的代理ips
        live_ips = list(set(old_ips_proxies + live_ips))
        with open("/home/www/htdocs/ips_proxies.txt","w+") as f:
            for i in live_ips:
                f.write(i)
                f.write("\n")
        f.close()
check_ip_proxy().run()


