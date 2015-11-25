#coding:utf-8

'''
readme

百度移动排名查询主程序  --->
1、从阿里云RDS中随机抽取关键词（按词类循环）
2、根据当前要查询的关键词类型，将从RDS中抽取的词拼接成对应的Query，并输出至固定文件
3、Scrapy读取固定文件，查询结果写入RDS
4、分析程序（analytics.py）读取RDS中查询结果，输出与JS图标相匹配的字段及数据，写入aoyouhost的mysql中

'''

import MySQLdb as mdb
import sys,os,time
from email.mime.text import MIMEText
import smtplib

reload(sys)
sys.setdefaultencoding('utf-8')

'''爬虫抓取百度wap端搜索结果'''
os.system(" scrapy crawl dmoz ")

'''提取当日抓取的排名数据'''
mysql_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
# mysql_time = '2015-11-16'

class_list = ['公司简介','公司工资','公司待遇','公司面试','公司怎么样','公司招聘','岗位职责','职位就业前景','职位工资','职位面试','职位招聘','职位待遇']

con = mdb.connect(host="",user="",passwd="",db="",charset='utf8');
cur = con.cursor(mdb.cursors.DictCursor)

# for CLASS in class_list:
query_file = open('jieguo','w')
with con:
	
	cur.execute(" select domain,CLASS,query from baidu_mobile_rank where date = '%s' " % mysql_time )
	rows = cur.fetchall()

	for row in rows:
		line = '%s,%s,%s' % (row['domain'],row['CLASS'],row['query'])
		query_file.write(line + "\n")

query_file.close()

'''计算看准及竞品网站排名'''
result_dict = {}
for CLASS in class_list :
	number = int(os.popen(' cat jieguo|grep "%s"|awk -F"," \'!a[$3]++\'|wc -l ' % CLASS).read().strip())

	kanzhun_rank = int( os.popen(' cat jieguo|grep "%s"|grep "kanzhun.com"|awk -F"," \'!a[$3]++\'|wc -l ' % CLASS ).read().strip() )
	jobui_rank = int(os.popen(' cat jieguo|grep "%s"|grep "jobui.com"|awk -F"," \'!a[$3]++\'|wc -l ' % CLASS ).read().strip())			
	wealink_rank = int(os.popen(' cat jieguo|grep "%s"|grep "wealink.com"|awk -F"," \'!a[$3]++\'|wc -l ' % CLASS ).read().strip())

	if kanzhun_rank == 0:
		kanzhun = 0
	else:
		kanzhun = str(format(float(int(kanzhun_rank))/number,'.0%')).replace('%','')

	if jobui_rank == 0:
		jobui = 0
	else:
		jobui = str(format(float(int(jobui_rank))/number,'.0%')).replace('%','')

	if wealink_rank == 0:
		wealink = 0
	else:
		wealink = str(format(float(int(wealink_rank))/number,'.0%')).replace('%','')

	print kanzhun,jobui,wealink

	result_dict['%s' % CLASS] = {'kanzhun':kanzhun,'jobui':jobui,'wealink':wealink} 

'''排名结果写入mysql'''
sql = '''INSERT INTO baidu_mobile_sql VALUES ("%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''' % (
	mysql_time,
	result_dict['公司简介']['kanzhun'],
	result_dict['公司简介']['wealink'],
	result_dict['公司简介']['jobui'],
	result_dict['公司工资']['kanzhun'],
	result_dict['公司工资']['wealink'],
	result_dict['公司工资']['jobui'],
	result_dict['公司待遇']['kanzhun'],
	result_dict['公司待遇']['wealink'],
	result_dict['公司待遇']['jobui'],
	result_dict['公司面试']['kanzhun'],
	result_dict['公司面试']['wealink'],
	result_dict['公司面试']['jobui'],
	result_dict['公司怎么样']['kanzhun'],
	result_dict['公司怎么样']['wealink'],
	result_dict['公司怎么样']['jobui'],
	result_dict['公司招聘']['kanzhun'],
	result_dict['公司招聘']['wealink'],
	result_dict['公司招聘']['jobui'],
	result_dict['岗位职责']['kanzhun'],
	result_dict['岗位职责']['wealink'],
	result_dict['岗位职责']['jobui'],
	result_dict['职位就业前景']['kanzhun'],
	result_dict['职位就业前景']['wealink'],
	result_dict['职位就业前景']['jobui'],
	result_dict['职位工资']['kanzhun'],
	result_dict['职位工资']['wealink'],
	result_dict['职位工资']['jobui'],
	result_dict['职位面试']['kanzhun'], 
	result_dict['职位面试']['wealink'],
	result_dict['职位面试']['jobui'], 
	result_dict['职位招聘']['kanzhun'],
	result_dict['职位招聘']['wealink'],
	result_dict['职位招聘']['jobui'],
	result_dict['职位待遇']['kanzhun'],
	result_dict['职位待遇']['wealink'],
	result_dict['职位待遇']['jobui']
	)

print 'Import：%s' % sql
try:
	cur.execute(sql)
	con.commit()
	print 'done'
except:
    con.rollback()

con.close()


