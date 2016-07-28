#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys
import time
import datetime
import urllib
import urllib2
import cookielib
import ConfigParser
import Image
import re
import thread
import util.util
from prettytable import PrettyTable
from cookielib import LoadError


cookfilename = './cache/cookie.txt'
cookie = cookielib.MozillaCookieJar()
cookie.load(cookfilename, ignore_discard=True, ignore_expires=True)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

"""
req = urllib2.Request("http://96096kp.com/UpdateMember.aspx")
response = opener.open(req)
htmltext = response.read()
myItems = re.findall('txt_Name" type="text" value="(.*?)" id="ctl00_FartherMain_txt_Name"',htmltext,re.S) 
if len(myItems)>0 :
  print myItems[0]
print htmltext
"""


ISOTIMEFORMAT='%Y-%m-%d %X'
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('./cache/cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req = urllib2.Request('http://96096kp.com/UserData/MQCenterSale.aspx')
#利用urllib2的build_opener方法创建一个opener
postdata = urllib.urlencode({
    'StartStation' : '8001',
    #'StartStation' : '重庆南坪汽车站',
    'WaitStationCode' : '',
    'OpStation' : '-1',
    'OpAddress' : '-1',
    'SchDate' : tomorrow,
    'DstNode' : '永川',
    'SeatType' : '',
    'SchTime' : '00:30',
    'OperMode' : '',
    'SchCode' : '',
    'txtImgCode' : '',
    'cmd' : 'MQCenterGetClass',
    'isCheck' : 'false'
})

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4' 
#headers = { 'User-Agent' : user_agent }  
headers = { 'User-Agent' : user_agent,'Referer':'http://96096kp.com/TicketMain.aspx','DNT' : '1','Connection' : 'keep-alive' }
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#opener.addheaders = [headers]
opener.addheaders = [('User-agent', 'Mozilla/5.0'),('DNT', '1'),('Referer','http://96096kp.com/TicketMain.aspx')]
response = opener.open(req,postdata)

str0 = response.read()
str1 = util.util.todict(str0)
str2 = str1['data']
ticketrow = PrettyTable()
ticketrow_head = []
ticketrow_body = []
ticketrow_count = 0
for str3 in str2 : 
  ticketrow_body = []
  for k, v in str3.iteritems() :
    if k in ['SchMode','SchFuel','SchPrintSeat','SchBerth','SchBusType','SchLocalCode','SchDstNode','SchDiscPrice','SchStdPrice','SchStat','SchDist','SchNodeName','SchSeatCount','SchChild','SchCompCode','SchStationCode','SchWaitingRoom','SchBusBrandColor','SchCompName', 'SchInterval','SchGlobalCode','Notes','SchFirstTime','SchBusLevel', 'SchType','SchOperType','SchBusBrand','SchDstCity','SchLastTime',] :
      continue
    if ticketrow_count == 0 :
      ticketrow_head.append(k)
    ticketrow_body.append(v)
  if ticketrow_count == 0 :
    ticketrow.field_names = ticketrow_head
  ticketrow.add_row(ticketrow_body)
  ticketrow_count+=1
print ticketrow

