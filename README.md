# proxypool  
  
个人挂起的代理ips：http://youknowi.xin/ips_proxies.txt  
  
0 0 * * * rm -rf "/home/www/htdocs/check_ips.txt"   每天零点删除check_ips.txt 因为个人是a+写文件来进行叠加的  
0 * * * * python /var/ip_proxy/ip_proxies_crawl.py  每个小时爬取一次最新的ips并验证  
*/30 * * * * python /var/ip_proxy/check_ip_proxies.py  每隔30分钟检验一次ip的可用性  
0 3 * * 0 python /var/ip_proxy/check_all_ip_proxies.py  每天零点检验一次all_ips历史的ips哪些能用  （最后还是换成每周三点：0 3 * * 0）  
  
  