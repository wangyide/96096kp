#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Image
import os


class imgsimilar() :
  def getGray(self,image_file):
    tmpls=[]
    for h in range(0, image_file.size[1]):#h
      for w in range(0, image_file.size[0]):#w
        tmpls.append( image_file.getpixel((w,h)) )
       
    return tmpls
   
  def getAvg(self,ls):#获取平均灰度值
    return sum(ls)/len(ls)
   
  def getMH(self,a,b):#比较100个字符有几个字符相同
    dist = 0;
    for i in range(0,len(a)):
      if a[i]==b[i]:
        dist=dist+1
    return dist
   
  def getImgHash(self,fne):
    image_file = Image.open(fne) # 打开
    image_file=image_file.resize((12, 12))#重置图片大小我12px X 12px
    image_file=image_file.convert("L")#转256灰度图
    Grayls=self.getGray(image_file)#灰度集合
    avg=self.getAvg(Grayls)#灰度平均值
    bitls=''#接收获取0或1
    #除去变宽1px遍历像素
    for h in range(1, image_file.size[1]-1):#h
      for w in range(1, image_file.size[0]-1):#w
        if image_file.getpixel((w,h))>=avg:#像素的值比较平均值 大于记为1 小于记为0
          bitls=bitls+'1'
        else:
          bitls=bitls+'0'
    return bitls
  
  
  
  
def Smooth(Picture):
  BACKCOLOR=255
  '''平滑降噪'''
  Pixels = Picture.load()
  (Width, Height) = Picture.size
 
  xx = [1, 0, -1, 0]
  yy = [0, 1, 0, -1]
 
  for i in xrange(Width):
    for j in xrange(Height):
      if Pixels[i, j] != BACKCOLOR:
        Count = 0
        for k in xrange(4):
          try:
            if Pixels[i + xx[k], j + yy[k]] == BACKCOLOR:
              Count += 1
          except IndexError: # 忽略访问越界的情况
            pass
        if Count > 3:
          Pixels[i, j] = BACKCOLOR
  return Picture



def img_to_list(img) :
  width,high = img.size
  pix=Smooth(img.convert(mode="1")).load()

  matrix = [None]*high
  for i in range(len(matrix)) :
    matrix[i] = [0]*width

  for i in range(high) :
    for j in range(width) :
      matrix[i][j]=1-min(pix[j,i],1)
  # print matrix[1]
  return matrix

def imgsame(a=[],b=[]) :
  diff=0
  if len(a) != len(b) or len(a[0]) != len(b[0]) :
    diff = 10000
  else :
    for i in range(len(a)) :
      for j in range(len(a[0])) :
        if a[i][j] != b[i][j] :
          diff+=1
  return diff
