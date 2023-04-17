import pandas as pd
import numpy as np

# 读取csv文件，文件路径根据实际情况修改
df = pd.read_csv('E:\自己玩的数据\数据可视化\WorldCupMatches.csv', encoding='utf-8')
df1 = pd.read_csv('E:\自己玩的数据\数据可视化\WorldCupPlayers.csv', encoding='utf-8')
df2 = pd.read_csv('E:\自己玩的数据\数据可视化\WorldCupsSummary.csv', encoding='utf-8')

# 查看数据的描述统计信息
print(df.describe(),df1.describe(),df2.describe())
# 查看是否有空值
print(df.isnull().sum(),df1.isnull().sum(),df2.isnull().sum())
# 查看是否有异常值
print(df.describe().loc[['min', 'max']],df1.describe().loc[['min', 'max']],df2.describe().loc[['min', 'max']])
# 删除重复值
df.drop_duplicates(inplace=True)
df1.drop_duplicates(inplace=True)
df2.drop_duplicates(inplace=True)
# 查看是否有空白值
print(df.isna().sum(),df1.isna().sum(),df2.isna().sum())

import pandas as pd
import matplotlib.pyplot as plt
# 取出现场观众总人数列
attendance = df['Attendance']
# 绘制直方图
plt.hist(attendance, bins=20, color='skyblue')
# 添加标题和轴标签
plt.title('World Cup Attendance Histogram')
plt.xlabel('Attendance')
plt.ylabel('Frequency')
# 显示图形
plt.show()


# 按照冠军国家队所在洲对数据进行分组，然后计算每个洲的现场观赛总人数
continent_attendance = df.groupby(['WinnerContinent'])['Attendance'].sum()

# 绘制柱状图
continent_attendance.plot(kind='bar')
plt.xlabel('Continent of Winning Team')
plt.ylabel('Total Attendance')
plt.title('Total Attendance by Continent of Winning Team')
plt.show()


import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 获取城市列
cities = df["City"].dropna().astype(str)

# 分词
words = " ".join(jieba.cut(" ".join(cities)))

# 准备足球形状的图片
mask = np.array(Image.open("./数据可视化/soccer.png"))

# 生成词云图
wc = WordCloud(width=800, height=400, background_color="white", max_words=2000, font_path="msyh.ttc", mask=mask).generate(words)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()























