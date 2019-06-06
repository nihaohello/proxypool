#coding=utf-8
import requests
import time
import random
class check_ip_proxy(object):
    def __init__(self):
        pass
    def run(self):
        f = open("/home/www/htdocs/ips_proxies.txt")
        old_ips = []
        for i in f.readlines():
            old_ips.append(i.rstrip("\n"))
        f.close()
        # print(old_ips)
        self.check_ip(old_ips)
    def check_ip(self,ips):
        live_ips=[]
        for ip in ips:
            if "https" in ip:
                try:
                    s = requests.get('http://www.baidu.com/', proxies={"https":str(ip)}, timeout=2)
                    if s.status_code == 200:
                        print("成功" + ":" + (str(ip)))
                        # self.file_save(str("https://" + ip))
                        live_ips.append(str(ip))
                except Exception as e:
                    pass
            else:
                try:
                    s = requests.get('https://www.baidu.com/', proxies={"http":str(ip)}, timeout=2)
                    if s.status_code == 200:
                        print("成功" + ":" + (str(ip)))
                        # self.file_save(str("http://" + ip))
                        live_ips.append(str(ip))
                except Exception as e:
                    pass
    # def file_save(self,ip):
        if len(live_ips)==0:
            live_ips=ips
        live_ips=list(set(live_ips))
        with open("/home/www/htdocs/ips_proxies.txt","w+") as f:
            for i in live_ips:
                f.write(ip)
                f.write("\n")
        f.close()
check_ip_proxy().run()


