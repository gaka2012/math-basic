#!/usr/bin/python
# -*- coding:UTF-8 -*-

import numpy as np

#基础加减乘操作
'''
ma1=np.mat([[1,-1,2],[1,0,3],[-1,2,-1]]) #matrix的缩写，直接就是矩阵形式。也可以用array,也是矩阵形式。但是计算过程不一样！！！！
ma2=np.mat([[1,1],[2,-1],[3,2]])
transma1=np.transpose(ma1) #矩阵的转置 transposition
#masum=ma1+ma2  #加法和减法中 mat和array的结果时一样的，但是乘法就不同了。
#masub=ma1-ma2
mamul=ma1*ma2  #mat算法是真正的矩阵算法，但是array是简单的点积。
print (mamul)
print (np.transpose(ma2)*np.transpose(ma1))
'''
'''
#求解特征值和特征向量 #行列式
#注意:矩阵的特征值和等于矩阵的迹
ma11=np.mat([[4,0,0],[0,3,1],[0,1,3]])
eig=np.linalg.eig(ma11)#求特征值和特征向量
tr=np.trace(ma11)      #求迹
print (tr,eig)

#以下是求得的结果，特征有3个，分别是4，2，4（有2个是一样的）
#特征向量要竖着看，4对应的特征向量是 0，1，1
#                 2对应的特征向量是 0，1，-1
#                 4对应的另一个特征向量是1，0，0
'''
'''
(array([4., 2., 4.]), array([[ 0.        ,  0.        ,  1.        ],
       [ 0.70710678,  0.70710678,  0.        ],
       [ 0.70710678, -0.70710678,  0.        ]]))
'''

ma=np.mat([[-0.233,-0.24,0.06],[-0.24,-0.717,-0.451],[0.06,-0.451,0.95]])
eig=np.linalg.eig(ma)
print (eig)

'''
xx,xy,xz,yy,yz,zz=-0.233,-0.24,0.06,-0.717,-0.451,0.95
yx=xy
zx=xz
zy=yz
M0=((xx*xx+xy*xy+xz*xz+yx*yx+yy*yy+yz*yz+zx*zx+zy*zy+zx*zx)/2)**0.5
print (M0) 
