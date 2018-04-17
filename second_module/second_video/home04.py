#coding:utf-8
'''
4. re （编程） 利用re模块
124.127.244.4 - - [07/Nov/2017:10:15:02 +0800] "GET /api/v1/interested_tag/ HTTP/1.0" 200 188 "http://luffy.oldboyedu.com/" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
124.127.244.4 - - [07/Nov/2017:10:15:02 +0800] "GET /api/v1/industry/ HTTP/1.0" 200 456 "http://luffy.oldboyedu.com/" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
124.127.244.4 - - [07/Nov/2017:10:15:02 +0800] "GET /api/v1/ip_info/ HTTP/1.0" 200 111 "http://luffy.oldboyedu.com/" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
124.127.244.4 - - [07/Nov/2017:10:15:02 +0800] "GET /api/v1/province/ HTTP/1.0" 200 423 "http://luffy.oldboyedu.com/" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
124.127.244.4 - - [07/Nov/2017:10:15:02 +0800] "GET /api/v1/captcha_check/?t=1510020901753 HTTP/1.0" 200 122 "http://luffy.oldboyedu.com/" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
把IP地址过滤出来。

'''

import re,io

read_file = io.open('log.txt','r',encoding='utf-8')

for line in read_file.readlines():
    res = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",line)
    print(res)
