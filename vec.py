# #AMPS-1D说明
# ------------------------
# #材料参数
# 基于泊松方程，电子和空穴的连续性方程，以及符合/产生方程。
# ##半导体材料参数


# ##DOS图像
# 输入量：禁带中缺陷的分布和各空间区域的变化
#         交叉捕获面积的信息-量化多种缺陷对于电子和空穴的吸引能力
# ###半导体物理中杂质掺杂
# 方式：扩散和离子注入


# #单晶半导体参数
# 1. 能带参数
#    决定因素：材料层的能带有效状态密度Nv和Nc，电子亲和能Xe,禁带宽度Eg，x=L处的势垒高度$$,和半导体中靠近x=L这个接触的电子亲和能。

# 2. 定域(禁带中)参数
#    实际上，禁带中还存在着很多不同类型的能级，即是材料是单晶材料。AMPS把能级归为二类：一类是缺陷（结构和杂质）引起的，一类是有意地掺杂引起的。二类可能会有类施主态和类受主态。
# *掺杂能级的参数*   包括离散的能级和具有一定宽度（较高的能级边界和较低的能级边界之间）的带能级。
#    **离散掺杂能级参数***
#    ----------------------------------
#          参数设置：各能级上受主与施主的浓度$$,各能级距离导带和价带的距离$$以及各能级的交叉捕获面积$$
#    **带掺杂能级参数**
#    -----------------------------------
#          参数设置：第i层的能级参数$$、浓度$$和交叉捕获面积$$
# *缺陷能级的参数*
#     AMPS模拟一些具有连续的方程形式(指数式、高斯式、常数式)的能级
#     **离散和类缺陷能级的参数***
#     -------------------------------------
#       设置
#     **连续缺陷能级的参数***     禁带中连续分布的定域能级
#     -------------------------------
#       类型：指数型、高斯型、常数型
#       1. 指数型
#             设置：决定状态数的参数-带尾斜率的特征能级和单位体积单位能级的状态数，同时设置带尾中电子和空穴的交叉捕获面积
#       2. 高斯型

#       3. 常数型
# *光特性参数*
#       材料的光吸收系数和相对介电常数
# -*- coding:utf-8 -*-
----------------------------------------------
def linear(a,b):
  def result(x):
    return a*x+b
  return result
  """等价
  """
class linear:
  def __init__(self,a,b):
    self.a,self.b=a,b

  def __call__(self,x):
    return self.a*x+self.a
----------------------------------------
#文件读取
fobj=open("sample.txt")
fobj.read()#文件整个读取
fobj.readline()#每次读取文件的一行
fobj.readlines()#读取所有行到一个列表中
#遍历文件对象来读取文件中的每一行
for x in fobj:
  print(x,end=' ')
#通过write()方法写入文件，'w'
fobj.close()

#with语句
with open('sample.txt') as fobj:
  for line in fobj:
    print(line,end=' ')
--------------------------------------------
from enthought.traits.api import HasTraits,Color
-------------------------------------------------------
#python装饰器联系
#最初代码
class bol(object):
  def __init__(self,func):
    self.func=func

  def __call__(self):
    return "<b>{}</b>".format(self.func())

class ita(object):
  def __init__(self,func):
    self.func=func
  def __call__(self):
    return "<i>{}</i>".format(self.func())

@bol
@ita
def sayhi():
  return 'hi'
-------------------------------------------------------------
#改进一
class sty(object):
  def __init__(self,tag):
    self.tag=tag

  def __call__(self,f):
    def wraper():
      return "<{tag}>{res}</{tag}>".format(res=f{},tag=self.tag)
    return wraper

@sty('b')
@sty('i')
def sayhi():
  return 'hi'
---------------------------------------------------------------
#从指定URL中下载文件的程序
#!/usr/bin/env python3
import os
import os.path
import requests

def download(url):
  '''
  从指定的URL中下载并存储到当前目录
  ：arg url:要下载的文件的URL
  '''
  req=requests.get(url)
  if req.status_code==404:
    print('No such file found at %s' % url)
    return
  filename=url.split('/')[-1]
  with open(filename,'wb') as fobj:
    fobj.write(req.content)
  print("Download over.")

if __name__=='__main__':
  url=input('Enter a URL:')
  download(url)

----------------------------------------------------------
#斐波那契数列
def fibonacci(n):
  a=b=1
  for i in range(n):
    yield a  #yield meaning?
    a,b=b,a+b

-----------------------------------------
! 处理文件路径
import os


-------------------------------------------