import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dt = open('C:/Users/mypython/Desktop/10.csv')
#程序与文件夹同目录,默认读取utf-8,现读取方式为gbk
data = pd.read_csv(dt)
data.head()#简单查看

x = data[['发电总效率','炼焦总效率','炼油总效率']].values
y = data[['总效率']].values.reshape(-1, 1)
m = len(x)
n = 4
b = np.ones(m)
X = np.insert(x,0,b,axis=1)

def fun(theta):
    return 1/(2*m)*np.sum([(X[i]@theta-y[i])**2 for i in range(m)])

def gfun(theta):
    return 1/m*np.sum([(X[i]@theta-y[i])*X[i].reshape(-1, 1) 
                       for i in range(m)],axis=0)

#定义Hesse矩阵
def G(theta):
    return 1/m*sum([X[i].reshape(-1,1)*X[i] for i in range(m)])

#非精确线搜索
def Armijo(xk,dk):
    beta=0.5;sigma=0.2;m=0;maxm=20;mk=0;
    while m<maxm:
        if fun(xk+beta**m*dk)<=fun(xk)+sigma*beta**m*gfun(xk).T@dk:
            mk=m
            break
        m +=1
    newxk=xk+beta**mk*dk
    return newxk,mk

theta = 0.15*np.ones(n).reshape(-1,1)
epsilon = 10**(-5)
maxn = 0

while maxn < 20000:
    gk = gfun(theta)
    dk = -gk
    [theta,mk] = Armijo(theta,dk)
    if np.linalg.norm(gk)<10**(-5):
        break   
    print('第%s次迭代，梯度范数：'%maxn,np.linalg.norm(gk),'极小点是：',
          theta,'函数值：',fun(theta))
    maxn += 1
R2 = 1-fun(theta)*2*m/np.sum([(y[i]-np.mean(y))**2 for i in range(m)])
R2_adjusted = 1-(1-R2)*(m-1)/(m-3-1)

print('预测绝对误差为：',np.sqrt(fun(theta)*2*m))
print('预测相对误差为：',np.sqrt(fun(theta)*2)/np.mean(np.abs(y)))
print('决定系数为：',R2)
print('校正决定系数为：',R2_adjusted)
