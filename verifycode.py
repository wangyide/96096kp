#!/usr/bin/python2.7
# -*- coding:utf-8 -*-


import Image
import sys
import os
import shutil
import time
import util.imgutil as imgutil

class Vcode :
  def __init__(self) :
    pass

  def xor(self,i,j) :
    if i>0 and j>0 or i==0 and j==0 :
      return 0
    else :
      return 1

  def orc(self,im='') :
    
    code=[]
#     读取字模，保存到字符矩阵
    dic={}
    files = os.listdir("./dic")
    for f in files :
#     print f[0]
        dic[f[0]]=imgutil.img_to_list(Image.open('dic/'+f))
        
#     将图片二值化、降噪、裁剪、矩阵化
    img = imgutil.Smooth(Image.open(im).convert(mode="1")).crop((0,5,50,18))
    matrix = imgutil.img_to_list(img)
    width,high = img.size
    
#     计算图片的投影
    for i in range(width) :
      for j in range(high-1) :
        matrix[12][i]+=matrix[j][i]
#     print matrix[12]
    
    
#     通过投影进行切割
    aaa=[]
    for i in range(width-1) :
        if self.xor(matrix[high-1][i],matrix[high-1][i+1]) == 1 :
            aaa.append(i+1)

#      裁剪后的矩阵存入4个c
    if len(aaa)<8 :
        return None
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    cc=[c1,c2,c3,c4]
    for i in range(high-1) :
        c1.append(matrix[i][aaa[0]:aaa[1]])
        c2.append(matrix[i][aaa[2]:aaa[3]])
        c3.append(matrix[i][aaa[4]:aaa[5]])
        c4.append(matrix[i][aaa[6]:aaa[7]])

    for c in cc :
        result=['*',1000]
        for name,value in dic.iteritems() :
            sam = imgutil.imgsame(c,value)
#             像素相差10以上就判为失败，越小越精确
            if sam >10 :
                continue
#             print 'sam',sam
            if  sam< result[1] :
                result[0]=name
                result[1]=sam
#         print result
        if result[0] == '*' :
            return None
        code.append(result[0])
    return ''.join(code)

if __name__ == '__main__' :
  vcode = Vcode()
  print vcode.orc(os.path.join('cache','96096kp_vcode.gif'))

