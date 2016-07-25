#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys
import time
import urllib
import urllib2
import cookielib
import ConfigParser
import Image
import re
import thread
from cookielib import LoadError

import verifycode


class Login :

  def __init__(self) :
    self.cookfilename = './cache/cookie.txt'
    self.loginName = ''

    #新建相关目录
    if os.path.exists('./cache') :
      if os.path.isdir('./cache') :
        print "Directory cache already exists, Program continue ..."
      else :
        print 'A file existing: %s' % os.getcwd() + '/cache'
        print 'Please check again'
        sys.exit(0)
    else :
      try :
        os.makedirs("./cache")
        print "Build directory cache successful, Program continue ..."
      except IOError,e:
        print e
        print 'Please check again'
        sys.exit(0)

    try:
      open(self.cookfilename, 'a').close()
    except IOError,e:
      print e
      sys.exit(0)

    try:
      self.cookie = cookielib.MozillaCookieJar()
      self.cookie.load(self.cookfilename, ignore_discard=True, ignore_expires=True)
    except LoadError,e :
      print "There",e
      self.cookie = cookielib.MozillaCookieJar(self.cookfilename)
      print self.cookie
    self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))


  def login(self) :
  #调用三种方式进行登录，依次为 1:cookie   2:自动识别验证码   3:手动输入验证码
    if self.loginByCookie() :
      pass
    elif self.loginByMachine() :
      pass
    elif self.loginByHand() :
      pass
    else :
      print 'End ...'
      sys.exit(0)



  def loginByCookie(self) :
  #通过旧cookie尝试登录
    vcodeUrl='http://96096kp.com/ValidateCode.aspx'
    result = self.opener.open(vcodeUrl)

    self.cookie.save(filename=self.cookfilename,ignore_discard=True, ignore_expires=True)
    self.loginName = self.getName()

    if self.loginName <> None :
      print '%s has alreadly logined! login success!!! ------login()' % (self.loginName)
      return True

  def loginByMachine(self) :
  #通过自动识别验证码尝试登录
    vcodeUrl='http://96096kp.com/ValidateCode.aspx'
    configfile = ConfigParser.ConfigParser()
    configfile.readfp(open("./cache/web.ini", "r"))
    for i in range(0,50) :
      result = self.opener.open(vcodeUrl)
      vcodef=open('./cache/96096kp_vcode.gif','wb+')
      vcodef.write(result.read()) 
      vcodef.close()
      image = Image.open("./cache/96096kp_vcode.gif")
      vcode = verifycode.Vcode().orc(os.path.join('./cache','96096kp_vcode.gif'))
      if vcode is None :
        time.sleep(2)
        print vcode,'第 %s 次登录失败,2s 后程序继续...' % (i+1)
        continue
      postdata = urllib.urlencode({
            'LoginID':configfile.get("account", "username"),
            'LoginPwd':configfile.get("account", "password"),
            'LoginValid':vcode,
            'getInfo': 0,
            'cmd': 'Login'
          })
      gradeUrl = 'http://96096kp.com/UserData/UserCmd.aspx'
      result = self.opener.open(gradeUrl,postdata)
      if self.checkLogin() :
        print 'Successful Login in ....'
        return True
      print vcode,'第 %s 次登录失败,5s 后程序继续...' % (i+1)
      time.sleep(5)
    print 'Faild Login in ....'
    return False
 


  def loginByHand(self) :
  #手动输入验证码登录
    vcodeUrl='http://96096kp.com/ValidateCode.aspx'
    configfile = ConfigParser.ConfigParser()
    configfile.readfp(open("./cache/web.ini", "r"))
    result = self.opener.open(vcodeUrl)
    vcodef=open('./cache/96096kp_vcode.gif','wb+')
    
    vcodef.write(result.read()) 
    vcodef.close()
    
    image = Image.open("./cache/96096kp_vcode.gif")
    image.show()
    
    vcode = raw_input("Please input the vcode:")
    configfile = ConfigParser.ConfigParser()
    configfile.readfp(open("./cache/web.ini", "r"))
    postdata = urllib.urlencode({
          'LoginID':configfile.get("account", "username"),
          'LoginPwd':configfile.get("account", "password"),
          'LoginValid':vcode,
          'getInfo': 0,
          'cmd': 'Login'
        })
    
    gradeUrl = 'http://96096kp.com/UserData/UserCmd.aspx'
    #登录地址
    result = self.opener.open(gradeUrl,postdata)
    resultHtml = result.read()
    
    #myItems = re.findall('<div.*?class="content">(.*?)<.*?2015(.*?).*?></div>',resultHtml,re.S)
    if resultHtml == '{success:false,msg:"请正确输入验证码！"}' :
      print 'Login Failed'
    #{success:false,msg:"请正确输入验证码！"}
    myItems = re.findall('.*?"(.*?)".*?',resultHtml,re.S)
    self.name = myItems[0]
    print ' login success' 



  def getName(self) :
  #获取登录账号用户名
    cookie = self.cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

    #创建请求的request
    req = urllib2.Request("http://96096kp.com/UpdateMember.aspx")

    response = opener.open(req)
    htmltext = response.read()
    myItems = re.findall('txt_Name" type="text" value="(.*?)" id="ctl00_FartherMain_txt_Name"',htmltext,re.S) 
    if len(myItems)>0 :
      return myItems[0]
    return None

  def checkLogin(self) :
  #用于判断是否登录成功
    if self.getName() :
      return True
    else :
      return False


if __name__ == '__main__' :
  login=Login()
  login.login()
