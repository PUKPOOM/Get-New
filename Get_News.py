##### User Added Module #####
from bs4 import BeautifulSoup as soup 		# import BeautifulSoup fnc from bs4 located in C:\Python37\Lib\site-packages
import matplotlib.pyplot as plot 			# import pyplot.py in folder matplotlib located in C:\Python37\Lib\site-packages
import Send_Line as sl

##### Embedded Module #####
from urllib.request import urlopen as req	# import urlopen fnc from request.py in urllib located in C:\Python37\Lib\urllib
import csv 									# import csv.py in C:\Python37\Lib
import os.path								# import os.py in C:\Python37\Lib
##from datetime import datetime 				# import datetime from datetime.py
from datetime import * 						# import every module from datetime.py
import re 									# import Regular Expression module

def Get_Matichon(number_of_news):
	'Start Get_Matichon'
	print('\n##### M A T I C H O N | S T A R T #####')

	url = 'https://www.matichon.co.th/home'		# set url link
	web_open = req(url)							# object the web_open = req(url) from urlopen
	data_html = web_open.read()					# read opened url to data_html
	web_open.close()							# close the opened url
	##print("Closed or not : ", web_open.closed)	# check is it closed

	raw_data = soup(data_html,'html.parser')	# parser the html data
	new = raw_data.findAll('h3' ,{'class':'entry-title td-module-title'})		# find the your data from html page by right click & inspect, see the class
	'''
	<h3 class="entry-title td-module-title">
	<a href="https://www.matichon.co.th/court-news/news_1340964" rel="bookmark" title="..."></a>
	</h3>
	'''
	new_time = raw_data.findAll('span', {'class':'td-post-date'})	# find data's date from html	
	'''
	<span class="td-post-date"><time class="entry-date updated td-module-date" datetime="2019-01-30T10:53:06+00:00">วันที่ 30 มกราคม 2562 - 10:53 น.</time></span>
	'''	
	title = raw_data.findAll('div', {'class':'td_web_title'})		# find title source from html
	'''
	<div class="td_web_title">
    <a href="https://www.matichon.co.th">มติชนออนไลน์</a>
	</div>
	'''
	date = raw_data.findAll('div', {'class':'td_data_time'})
	'''
	<div class="td_data_time">วันพุธที่ 30 มกราคม 2562</div>
	'''	
	for row in title:					# need to do for loop because title is not 1 dimension
		http = row.a['href']			# got "https://www.matichon.co.th"
		news_title = row.findAll('a')	# got "<a href="https://www.matichon.co.th">มติชนออนไลน์</a>"
	news_title = news_title[0].text		# got "มติชนออนไลน์"
	for row in date:
		new_date = row.findAll('div', {'style':'visibility:hidden;'})	# <div style="visibility:hidden;">วันพุธที่ 30 มกราคม 2562</div>
	new_date = new_date[0].text
	##print(new)
	##print(new_time)
	##print(news_title)
	##print(new_date)

	# prepare the lists of data
	new_list = []
	new_link_list = []
	new_time_list = []
	for row in new:
		new_list.append(row.text)			# save news text to list
		new_link_list.append(row.a['href'])	# save news utl to list
	for row in new_time:
		new_time_list.append((row.text))	# save news time to list
	##print(new_list[0])
	##print(new_link_list[0])
	##print(new_time_list[0])

	return (new_list, new_link_list, new_time_list, news_title)

##############################################################
#				M A T I C H O N | D A T A
##############################################################
number_of_news = 10
news_list, news_link_list, news_time_list, news_title = Get_Matichon(number_of_news)
cnt = len(news_list)
##print('count of list = {}' .format(cnt))

##token = 'JX4I5WJmNYMXxPKBWJQW84FwJXjWNHMPVkKE82RBvbu'		# token to PukkyZ
token = 'yjpgHCeVZqNFygCJdBMAfhe152kFayp4nzL27w7C3Q4'		# token to Mhee Tui Group

print('\n##### M A T I C H O N | D A T A #####')
print('Top {} Hilight News from {} {}' .format(number_of_news, news_title, news_time_list[0]))
for i in range(number_of_news):
	print('{}.{}' .format(i+1,news_list[i]))
	sl.SendLine(token, news_list[i])
print('##### M A T I C H O N | E N D #####\n')