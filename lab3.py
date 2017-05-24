#! /usr/bin/env python
# -*- coding:utf-8 -*-

import xlrd
import xlwt
import urllib
from urllib2 import urlopen
import time
from selenium import webdriver
import json
import lxml.html as lxml
from xlutils.copy import copy


url = "https://twitter.com/english"
dev=[]
def write_xls(t,d,r,l):
    readbook = xlrd.open_workbook(r"/Users/Alexandr/Downloads/1/lab3_web/data_3.xls", on_demand=True, formatting_info=True)
    readsheet = readbook.sheet_by_index(0)
    writebook = copy(readbook)
    writesheet = writebook.get_sheet(0)  
    for i in range(len(t)):
        writesheet.write(i, 0, t[i])
        writesheet.write(i, 1, d[i])
        writesheet.write(i, 2, r[i])
        writesheet.write(i, 3, l[i])
        i=i+1
    readbook.release_resources()  
    writebook.save('/Users/Alexandr/Downloads/1/lab3_web/data_3.xls')
def getURL(url):
    s = 'error'
    try:
        f = urllib.request.urlopen(url)
        s = f.read()
    except urllib.error.HTTPError:
        s = 'not found'
    except urllib.error.URLError:
        s = 'url error'
    return s
def alert():

    word = "English"
    for i in range (len(text)):
        t = text[i]
        if t.find(word)>0:
            print ("{} detected at {}".format(word,dtime[i]))
            i = i + 1

'''json.position
#position = 353800710229471232
position = 0
url_add = "timeline/tweets?include_available_features=1&include_entities=1&max_position={}&reset_error_state=false".format(position)
url_res = url + url_add
response = urlopen(url_res)
data = json.load(response)
has_more = data['has_more_items']
#print (has_more)
while has_more!="False":
    position = position+1
    print(position)
print (position)
print (has_more)
'''

text = dtime = retw = likes = []
# Get scroll height
driver = webdriver.Chrome('/Users/Alexandr/Downloads/chromedriver')
driver.get(url)
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    SCROLL_PAUSE_TIME = 3
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
data = driver.page_source
driver.quit()
i=0
doc = lxml.fromstring(data)

readbook = xlrd.open_workbook(r"/Users/Alexandr/Downloads/1/lab3_web/data_3.xls", on_demand=True, formatting_info=True)
readsheet = readbook.sheet_by_index(0)
writebook = copy(readbook)
writesheet = writebook.get_sheet(0)

#print (doc.text_content())
for i in range (13):
    text_ = doc.xpath('//div[@class="js-tweet-text-container"]')[i].text_content()
    writesheet.write(i, 0, text_)
    text.append(text_)
    time_ = doc.xpath('//span[@class="_timestamp js-short-timestamp "]')[i].text_content()
    writesheet.write(i, 1, time_.strip())
    dtime.append(time_.strip())
    retw_ = doc.xpath('//span[@class="ProfileTweet-action--retweet u-hiddenVisually"]')[i].text_content()
    writesheet.write(i, 2, retw_.strip())
    #retw.append(retw_)
    likes_ = doc.xpath('//span[@class="ProfileTweet-action--favorite u-hiddenVisually"]')[i].text_content()
    writesheet.write(i, 3, likes_.strip())
    #likes.append(likes_)
    i=i+1
readbook.release_resources()
writebook.save('/Users/Alexandr/Downloads/1/lab3_web/data_3.xls')

alert()
