#coding:utf-8

import scrapy,re,urllib,os,time,sys
from ceshi_mobile.items import CeshiMobileItem
import MySQLdb as mdb

reload(sys)
sys.setdefaultencoding('utf8')

def search(req,line):
    text = re.search(req,line)
    if text:
        data = text.group(1)
    else:
        data = 'no'
    return data

mysql_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

class_dict = {	
				'公司简介':'',
				'公司工资':'工资',
				'公司待遇':'待遇',
				'公司面试':'面试',
				'公司怎么样':'怎么样',
				'公司招聘':'招聘',
				'岗位职责':'岗位职责',
				'职位就业前景':'就业前景',
				'职位工资':'工资',
				'职位面试':'面试',
				'职位招聘':'招聘',
				'职位待遇':'待遇'

				}

con = mdb.connect(host="",user="",passwd="",db="",charset='utf8');
query_file = open('/SEO_DATA/ceshi_mobile/query_file','w')
# query_file = open('/SEO_DATA/ceshi_mobile/query_file','w')

for k,v in class_dict.items():

	'''判断是读取company表还是job表'''
	if '公司' in k:
		table = 'company'
	else:
		table = 'job'

	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("select * from %s order by rand() limit 1000" % table)
		rows = cur.fetchall()

		print '-----------提取%s的关键词，输出至文件' % k
		for row in rows:
			query = '%s%s,%s' % (row['name'],v,k)
			query_file.write(query + "\n")

query_file.close()

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["m.baidu.com"]

	# start_urls = ['http://m.baidu.com/s?word=%E8%85%BE%E8%AE%AF%E6%8B%9B%E8%81%98&sa=tb&ts=6930998&t_kt=43&ss=101']

	start_urls = []
	for line in open('/SEO_DATA/ceshi_mobile/query_file'):
		line = line.strip()

		try:
			word = line.split(',')[0]
			CLASS = line.split(',')[1]
		except:
			print 'error'

		word = word.strip()
		url = 'http://m.baidu.com/s?word=%s&ts=4661497&t_kt=60&rsv_iqid=10316923837225262279&sa=ib&rsv_sug4=1424&ss=101&class=%s' % (urllib.quote(word),urllib.quote(CLASS) )
		start_urls.append(url)

	def __get_url_query(self, url):
		m =  re.search("word=(.*?)&", url).group(1)
		return m

	def __get_url_class(self, url):
		m =  re.search("class=(.*)", url).group(1)
		return m

	def parse(self,response):
		for sel in response.xpath('//*[@id="results"]/div'):
			query = urllib.unquote(self.__get_url_query(response.url))
			CLASS = urllib.unquote(self.__get_url_class(response.url))

			html = sel.extract().replace('\n','')
			srcid = ','.join(sel.xpath('.//@srcid').extract())
			#rank = ','.join(sel.xpath('.//@order').extract())
			rank = search(r'order="(\d+)"',html)

			if rank == 'no':
				title = ''
				domain = ''
			else:
				title = re.sub(r'<[^>]*?>','',','.join(sel.xpath('//*[@id="results"]/div[%s]/div[1]/a/h3' % int(round(float(rank)))).extract()))

			domain = search(r'div class="c-showurl"><span[^>]*?>(.*?)</span>',html)
			if domain == 'no':
				domain = search(r'<div class="c-showurl">(.*?)\s+\d+k</div>',html)
			if domain == 'no':
				domain = search(r'<span class="c-color-url">(.*?)</span>',html)
			if domain == 'no':
				domain = search(r'<div class="c-color-url">(.*?)</div>',html)
			if domain == 'no':
				domain = search(r'<span class="c-color-gray">(.*?)</span>',html)
			if domain == 'no':
				domain = '未知特型'

			item = CeshiMobileItem()

			item['rank'] = rank.encode()
			if title == '':
				item['title'] = title
			else:
				item['title'] = title.encode('utf-8')

			if domain == '':
				item['domain'] = domain
			else:
				item['domain'] = domain.encode('utf-8')

			item['date'] = mysql_time

			if srcid == '':
				item['srcid'] = srcid
			else:
				item['srcid'] = srcid.encode('utf-8')
		
			item['query'] = query
			item['CLASS'] = CLASS

			yield item

		print '%s done' % query
