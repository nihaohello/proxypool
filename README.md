# proxypool  
  
个人挂起的代理ips：http://youknowi.xin/ips_proxies.txt  
  
0 0 * * * rm -rf "/check_ips.txt"   每天零点删除check_ips.ttx  
0 * * * * python /ip_proxy_crawl.py  每个小时爬取一次最新的ips  
*/30 * * * * python /check_ip_proxy.py   每隔30分钟检验一次ip的可用性  
0 0 * * * python /check_ip_all.py   每天零点检验一次历史的ips哪些能用  （最后还是换成每周三点：0 3 * * 0）
  
  