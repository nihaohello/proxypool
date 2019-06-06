# proxypool  
  
个人挂起的代理ips：http://youknowi.xin/ips_proxies.txt  
  
0 0 * * * rm -rf "/home/www/htdocs/check_ips.txt"   每天零点删除check_ips.txt 因为个人是a+写文件来进行叠加的  
0 */4 * * * python /var/ip_proxy/ip_proxies_crawl.py  每隔开4小时爬取一次最新的ips并验证  
0 */2 * * * * python /var/ip_proxy/check_ip_proxies.py  每隔2小时检验一次ip的可用性  
0 1 * * 3 python /var/ip_proxy/check_all_ip_proxies.py  每天零点检验一次all_ips历史的ips哪些能用  （最后还是换成每周三点：0 3 * * 0）  
  
  
  
1.check_ips.txt  存放每小时爬取的ips  利用ip_proxies_crawl.py爬取西刺 快代理 iphai yunhai网站的当前存活ips  
2.all_ips.txt  存放上万的历史代理ips  check_all_ip_proxies每周三检测这个文件里ips的存活个数并保存  
3.ips_proxies.txt  存放当前能用的ips  check_ip_proxies.py每2小时检测一次存活性  
  
  