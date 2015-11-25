# -*- coding: utf-8 -*-

# Scrapy settings for ceshi_mobile project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import random,os,urllib2

BOT_NAME = 'ceshi_mobile'

SPIDER_MODULES = ['ceshi_mobile.spiders']
NEWSPIDER_MODULE = 'ceshi_mobile.spiders'

USER_AGENTS = [
    'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; MI 4LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1',
    'Mozilla/5.0 (iPhone 5CGLOBAL; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/6.0 MQQBrowser/5.8 Mobile/12F70 Safari/8536.25',
    'Mozilla/5.0 (Linux; Android 4.0.3; M031 Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a UCBrowser/9.3.1.339 Mobile',
    'Mozilla/5.0 (Linux; U; Android 4.1.1; zh-CN; M040 Build/JRO03H) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.4.1.362 U3/0.8.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/12B411 UCBrowser/10.1.0.518 Mobile WindVane tae_sdk_ios_1.0.1'
]

def getCookie():
    cookie_list = [
 	'MSA_WH=1436_475; BDUSS=JGalpwemU4enBPWTlWMExuelpQenpEWnk5VDRtT2F6bzN4SWF5a2ZJZ2tEMVZXQVFBQUFBJCQAAAAAAAAAAAEAAAAJkstJv7TXvMTj1NnM-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACSCLVYkgi1WMj; BDSFRCVID=-gDsJeCCxG3zWKQ4MMB2DuCenb7pCFhv-9Iq3J; H_BDCLCKID_SF=tbPHoK-5JCvqfR5k5KTSMtLQMfIX5-RLf-jMKPOF5lOTJh0R2lJv0j0IXtKH0nQm5Coa_-Jn3Jn-KDTVKjbke4tX-NFHJ6_DJM5; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; plus_lsv=72069d3a916adfdf; PLUS=1; lsv=globalTjs_b9e0763-wwwTcss_01779b4-wwwBcss_d0a2491-framejs_73bf934-globalBjs_32bfb16-sugjs_c44fc27-wwwjs_7b1626f; BDICON=10123156; H_WISE_SIDS=101505_100270_100272_101503_117_100294_100917; BAIDUID=791ED7F86F43AF44A3808AB244404E1A:FG=1',
    'MSA_WH=1436_475; BDUSS=JGalpwemU4enBPWTlWMExuelpQenpEWnk5VDRtT2F6bzN4SWF5a2ZJZ2tEMVZXQVFBQUFBJCQAAAAAAAAAAAEAAAAJkstJv7TXvMTj1NnM-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACSCLVYkgi1WMj; BDSFRCVID=-gDsJeCCxG3zWKQ4MMB2DuCenb7pCFhv-9Iq3J; H_BDCLCKID_SF=tbPHoK-5JCvqfR5k5KTSMtLQMfIX5-RLf-jMKPOF5lOTJh0R2lJv0j0IXtKH0nQm5Coa_-Jn3Jn-KDTVKjbke4tX-NFHJ6_DJM5; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; BDRCVFR[skC-pcPB0g_]=mk3SLVN4HKm; BDRCVFR[VjobkFsAYtR]=mk3SLVN4HKm; BDICON=10123156; lsv=globalTjs_b9e0763-wwwTcss_01779b4-wwwBcss_d0a2491-framejs_73bf934-globalBjs_32bfb16-sugjs_c44fc27-wwwjs_7b1626f; BAIDUID=791ED7F86F43AF44A3808AB244404E1A:FG=1; plus_lsv=72069d3a916adfdf; H_WISE_SIDS=101086_101011_100271_100173_100039_100764_100095_100107_100292_100920_100098; PLUS=1; __bsi=15977551608597644586_00_0_I_R_0_0303_C02F_N_I_I_0'
     ]
    cookie = random.choice(cookie_list)
    return cookie

PROXIES = []
for line in open('/home/wwwroot/default/hege_daili.txt'):
	line = line.strip()
	PROXIES.append({'ip_port':'%s' % line.strip() ,'user_pass':''})

# PROXIES = [
#	 {'ip_port': '111.11.228.75:80', 'user_pass': ''},
#	 {'ip_port': '120.198.243.22:80', 'user_pass': ''},
#	 {'ip_port': '111.8.60.9:8123', 'user_pass': ''},
#	 {'ip_port': '101.71.27.120:80', 'user_pass': ''},
#	 {'ip_port': '122.96.59.104:80', 'user_pass': ''},
#	 {'ip_port': '122.224.249.122:8088', 'user_pass': ''},
# ]

'''降低log级别，取消注释则输出抓取详情'''
LOG_LEVEL = 'INFO'

'''禁止cookie'''
COOKIES_ENABLED = False

'''启用cookie debug'''
COOKIES_DEBUG = True

'''下载中间件设置'''
DOWNLOADER_MIDDLEWARES = {
	# 'baidu_wap.middlewares.CustomDownloaderMiddleware': 543,
	'ceshi_mobile.middlewares.RandomUserAgent': 1,
	'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
	'ceshi_mobile.middlewares.ProxyMiddleware': 100,
	# 'scrapy_crawlera.CrawleraMiddleware': 600 	#crawlera设置
}

'''设置默认request headers'''
DEFAULT_REQUEST_HEADERS = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
	'Cache-Control':'no-cache',
	'Connection':'keep-alive',
	'Host':'m.baidu.com',
	'Pragma':'no-cache',
	'Referer':'http://m.baidu.com',
	'Upgrade-Insecure-Requests':'1',
    'Cookie':'%s' % getCookie()
}

'''下载延时，即下载两个页面的等待时间'''
DOWNLOAD_DELAY = 0.5

'''并发最大值'''
CONCURRENT_REQUESTS = 200

'''对单个网站并发最大值'''
CONCURRENT_REQUESTS_PER_DOMAIN = 200

# '''启用AutoThrottle扩展，默认为False'''
# AUTOTHROTTLE_ENABLED = True

'''设置下载超时'''
DOWNLOAD_TIMEOUT = 100

'''crawlera账号、密码'''
CRAWLERA_ENABLED = True
CRAWLERA_USER = '88aa8b802a7f4626b659dae926ee445b'
CRAWLERA_PASS = 'ab24562660'


MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'se_rank'
MYSQL_USER = 'root'
MYSQL_PASSWD = ''

ITEM_PIPELINES = {
    'ceshi_mobile.pipelines.CeshiMobilePipeline': 300,
    'ceshi_mobile.pipelines.MySQLCeshiMobilePipeline': 400,
}

