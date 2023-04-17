import pandas as pd
import  numpy as np
import seaborn as sns

data = pd.read_csv(r'E:\2020paper\Data visualization\医疗数据.csv',encoding="gbk")
data.head()

#检查数据
type(data)
shape = data.shape
print(data.shape)
print('数据集的行列数分别为:', shape[0], '行', shape[1], '列\n')   #行列数
data.isna().sum()    # 统计缺失值

#可视化缺失图
colours = ['#FF6347', '#ffff00']
sns.heatmap(data.isnull(), cmap=sns.color_palette(colours))

import missingno as msno
# 矩阵图：矩阵的nan矩阵是一个数据密集的显示，它可以让您快速地可视化地挑选出模式的数据完成。
msno.matrix(data.sample(250)) # 250表示需要显示的条数
# 柱形图：通过列来表示nan的简单方法:
msno.bar(data.sample(1000))
# 热力图：缺失无相关热图测量零相关:一个变量的存在或不存在对另一个变量存在的影响有多大
msno.heatmap(data)
# 树状图：可以让你更全面地将变量完成情况关联起来，比相关热图中的两两对比更深入地揭示趋势:
msno.dendrogram(data)

## 缺失率
data.isnull().sum(axis=0)/data.shape[0]
# 删除全空的行
data.dropna(how='all',inplace=True) 
data = data.dropna(axis=0) 
data.isna().sum()    # 统计缺失值

#其中很多数值符合线性回归所以用前后的均值填补
#填补数据
data['NL'] =  data['NL'].fillna(method='bfill')
data['XB'] =  data['XB'].fillna(method='bfill')
data['RYQH'] =  data['RYQH'].fillna(method='bfill')

data = data.dropna(axis=0) 
data.isna().sum()    # 统计缺失值


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# 接下里做一些可视化分析
# 区域分布,这里的划分比较乱，需要把他们统一划分到镇或者街道，这个应该是临沂市的区划
shuju = {'费县':'费县','兰山区':'兰山区','双堠镇':'沂南县','长城镇':'兰陵县','流峪镇':'平邑县','兰陵县':'兰陵县','夏蔚镇':'沂水县','四十里镇':'沂水县','沂水县':'沂水县','市本级':'市本级','郑城镇':'平邑县','山东省临沂市':'市本级','新庄镇':'费县','大兴镇':'临沭县','依汶镇':'沂南县','郯城县港上镇':'郯城县','温水镇':'平邑县','朱田镇':'费县','高新开发区':'高新区','上冶镇':'费县','姚店子镇':'沂水县','汤河':'河东区','临港产业区':'莒南县','孙祖镇':'沂南县','沂南县':'沂南县','圈里乡':'沂水县','平邑镇':'平邑县','郯城县马头镇':'郯城县','临沭县':'临沭县','莒南县':'莒南县','南桥镇':'兰陵县','高都街道办事处':'罗庄区','砖埠镇':'沂南县','青云镇':'临沭县','河东区':'河东区','湖头镇':'沂南县','车辋镇':'兰陵县','郯城县郯城镇':'郯城县','探沂镇':'费县','平邑县':'平邑县','费城镇':'费县','马庄镇':'费县','郯城县胜利乡':'郯城县','郯城县泉源乡':'郯城县','大仲村镇':'兰陵县','店头镇':'临沭县','郯城县马头镇高册':'郯城县','郯城县红花乡':'郯城县','下村乡':'兰陵县','郯城县':'郯城县','郯城县庙山镇':'郯城县','郯城县李庄镇':'郯城县','郯城县杨集镇':'郯城县','郯城县归昌乡':'郯城县','铜石镇':'平邑县','马站镇':'沂水县','杨庄镇':'沂水县','白彦镇':'平邑县','仲村镇':'平邑县','院东头镇':'沂水县','蒙山旅游区':'蒙阴县','大庄镇':'沂南县','玉山镇':'临沭县','许家湖镇':'沂水县','罗庄区':'罗庄区','诸葛镇':'沂水县','经济开发区':'经济开发区','郯城县重坊镇':'郯城县','泉庄镇':'沂水县','褚墩镇':'罗庄区','卞庄街道':'兰陵县','罗庄街道办事处':'罗庄区','马厂湖镇':'兰山区','临沭街道办':'临沭县','蒲汪镇':'沂南县','马牧池乡':'沂南县','地方镇':'平邑县','保太镇':'平邑县','富官庄镇':'沂水县','沂城街道办事处':'沂水县','高桥镇':'沂水县','沂堂镇':'罗庄区','临涧镇':'平邑县','张庄镇':'沂南县','卞桥镇':'平邑县','薛庄镇':'费县','曹庄镇':'临沭县','付庄街道办事处':'罗庄区','苏村镇':'沂南县','梁邱镇':'费县','磨山镇':'兰陵县','石门镇':'临沭县','兰陵镇':'兰陵县','黄山镇':'罗庄区','沙沟镇':'沂水县','丰阳镇':'平邑县','郑山街道办':'临沭县','武台镇':'平邑县','凤凰岭':'河东区','龙家圈镇':'沂水县','尚岩镇':'兰陵县','盛庄街道办事处':'罗庄区','新兴镇':'兰陵县','庄坞镇':'兰陵县','郯城县新村乡':'郯城县','向城镇':'兰陵县','岸堤镇':'沂南县','南张庄乡':'费县','胡阳镇':'费县','铜井镇':'沂南县','郯城县高峰头镇':'郯城县','大田庄乡':'费县','芦柞镇':'兰陵县','鲁城镇':'兰陵县','石井镇':'费县','汤头':'河东区','八湖':'河东区','矿坑镇':'兰陵县','神山镇':'兰陵县','联城':'蒙阴县','工业园':'工业园','辛集镇':'沂南县','相公':'河东区','郯城县花园乡':'郯城县','蛟龙镇':'临沭县','册山街道办事处':'罗庄区','郑旺':'河东区','蒙阴县':'蒙阴县','罗西办事处':'高新区','郯城县沙墩镇':'郯城县','太平':'河东区','青驼镇':'沂南县','界牌':'蒙阴县','高庄镇':'沂水县','金岭镇':'兰陵县','岱崮':'蒙阴县','崔家峪镇':'沂水县','蒙阴街道':'蒙阴县','高新区区直社区':'高新区','九曲':'河东区','桃墟':'蒙阴县','旧寨':'蒙阴县','垛庄':'蒙阴县','高都':'罗庄区','野店':'蒙阴县','道托镇':'沂水县'}
data['QH'] = data['RYQH'].map(shuju)

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

fig = plt.figure(figsize=(12,8))
plt.bar(range(16),data.QH.value_counts(),color='cyan',alpha=0.5)
plt.xlim(-1,16)
plt.title('人员区划统计')
for x,y in enumerate(data.QH.value_counts()):
    plt.text(x,y+100,y,ha='center')
plt.xticks(range(16),['兰山区','罗庄区','平邑县','莒南县','市本级','临沭县','沂水县','兰陵县','郯城县','费县','沂南县','高新区','河东区','蒙阴县','经济开发区','工业园'],rotation=30);

data['JZ'] = data['JZQH'].map(shuju)
fig = plt.figure(figsize=(12,8))
plt.bar(range(14),data.JZ.value_counts(),color='brown',alpha=0.4)
plt.xlim(-1,14)
plt.title('就诊区划统计')
for x,y in enumerate(data.JZ.value_counts()):
    plt.text(x,y+100,y,ha='center')
plt.xticks(range(14),['兰山区','市本级','罗庄区','平邑县','莒南县','沂水县','临沭县','兰陵县','郯城县','沂南县','费县','河东区','蒙阴县','高新区'],rotation=30);

fig = plt.figure()
plt.bar(range(2),data.XB.value_counts(),color='maroon',alpha=0.4)
plt.xlim(-1,2)
plt.title('分性别病患统计')
for x,y in enumerate(data.XB.value_counts()):
    plt.text(x,y+100,y,ha='center',fontsize=15)
plt.xticks(range(2),['男','女']);

dd = data[data.NL<7].ZDMC.value_counts().reset_index()
import squarify
fig = plt.figure(figsize=(10,8))
plot = squarify.plot(sizes = dd.ZDMC, # 指定绘图数据
                     label = dd[dd.ZDMC>30]['index'], # 指定标签
                     alpha = 0.6, # 指定透明度
                     value = dd[dd.ZDMC>30]['ZDMC'], # 添加数值标签
                     edgecolor = 'white', # 设置边界框为白色
                     linewidth =3 # 设置边框宽度为3
                    )

ddd = data[data.NL>70].ZDMC.value_counts().reset_index()
import squarify
fig = plt.figure(figsize=(10,8))
plot = squarify.plot(sizes = ddd.ZDMC, # 指定绘图数据
                     label = ddd[ddd.ZDMC>30]['index'], # 指定标签
                     alpha = 0.6, # 指定透明度
                     value = dd[dd.ZDMC>30]['ZDMC'], # 添加数值标签
                     edgecolor = 'white', # 设置边界框为白色
                     linewidth =3 # 设置边框宽度为3
                    )

# 为了做一个相关性分析，这里将一些字符型的字段，用sklearn转化成离散数字
import seaborn as sns 
from sklearn import preprocessing
enc = preprocessing.OrdinalEncoder()
fig = plt.figure(figsize=(12,8))
data[['XB','RYLB','YLLB','RYQH','JZQH','JGDJ','ZDMC']]=enc.fit_transform(data.loc[:,['XB','RYLB','YLLB','RYQH','JZQH','JGDJ','ZDMC']])
corr = data.corr()
sns.heatmap(corr,annot=True)


Cname=data['JGDJ']
 
num=np.array(range(0,len(Cname)))                                #用于记录每个地名重复出现次数
print(num)
print(Cname)
space=range(0,len(Cname))
print(space,type(space))
space=pd.DataFrame(space,columns=['name'])
space['name'][0]=(Cname[2])
print(space)
print(data['name'])                                         #取某一列
 
 
for i in range(len(Cname)):
    k = 0                                                      #记录次数
    for j in range(len(Cname)):
        if (Cname[i]==Cname[j]):
            space['name'][i]=Cname[j]
            k=k+1
        else:
            k=k
    num[i] = k
 
# print(space)
# print(num)
num=pd.DataFrame(data=num,columns=['num'])
# print(num)
frame=[space,num]                                                #concat进行两个dataframe合并
result=pd.concat(frame,axis=1)                                   #axis=1为向右连接，  =0 为向下连接
# print(result)
result=result.drop_duplicates('name',keep='first')   
