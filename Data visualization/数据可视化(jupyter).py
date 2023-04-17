import pandas as pd
import  numpy as np
import seaborn as sns

data = pd.read_csv(r'E:\2020paper\Data visualization\医疗数据.csv',encoding="gbk")
data.head()
data1 = {
    'ZMDC':['主动脉弓狭窄','动脉狭窄','股骨假体周围骨折','肝肿瘤','慢性丹囊炎','矽肺','膝关节滑膜囊肿','骨恶性肿瘤','主动脉瓣关闭不全','蛛网膜下腔出血'],
    'ZFY':[47772.13,24344.24,22613.36,21825.21,21037.6,20392.86,19665.33,19615.65,19194.55,18373.56]
}
df = pd.DataFrame(data1,index=['1','2','3','4','5','6','7','8','9','10'])
df.head()
df['ZMDC']
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
cc = list( df["ZMDC"].values ) 
cc
ccc = ['COA','ISR','Femur','HCC','ACC','SIS','Silicosis','TCGA','AR','SAH']
#画柱状图

values = []
for i in df.values:
    dic = {}
    dic["value"] = i[1]
    values.append(dic)


c = (
    Bar(init_opts=opts.InitOpts(width="750px", height="400px",theme = ThemeType.DARK ))
    .add_xaxis( ccc )
    .add_yaxis("平均花费金额", values, category_gap="40%")
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(22, 77, 167, 1)'
            }, {
                offset: 1,
                color: 'rgba(77, 160, 321, 1)'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(77, 160, 321)",
            }
        }
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="看病花费金额top10", pos_bottom = "87%", pos_right = "5%"))
    #.render("bar_border_radius.html")
)
c.render_notebook()
# 绘制动态榜单
month_lis = ['2019年12月','2020年1月','2020年2月']
month_data_lis = [month12_data,month1_data,month2_data]
color_function = """
        function (params) {
            if (params.value < 20000) 
                return ' #FF7256';
            else if (params.value >= 20000 && params.value < 40000) 
                return '#19ed95';
            else return '#3333cc';
        }
        """
# 新建一个timeline对象
t2 = Timeline(
        init_opts=opts.InitOpts(
            bg_color='#FFE4E1',  # 设置背景颜色
            theme='macarons',         # 设置主题
            width='900px',     # 设置图的宽度
            height='700px'     # 设置图的高度
        )
)
t2.add_schema(
    is_auto_play = True,    # 是否自动播放
    play_interval = 1500,   # 播放速度
    is_loop_play = True,   # 是否循环播放
)

for i,data1 in zip(month_lis,month_data_lis):
    day = i
    bar = Bar(
            init_opts=opts.InitOpts(
            bg_color='#FFE4E1',  # 设置背景颜色
            theme='essos',         # 设置主题
            width='1200px',     # 设置图的宽度
            height='600px'     # 设置图的高度
        )
    )
    bar.add_xaxis(data1['产品类别id'].tolist())
    bar.add_yaxis(
        '销售额', 
        data1['销售额'].round(2).tolist(),
        category_gap="40%"
        )
    bar.reversal_axis()
    bar.set_series_opts( # 自定义图表样式
        label_opts=opts.LabelOpts(is_show=True,position = "right"), # 是否显示数据标签
        itemstyle_opts={  
            "normal": {
                 "color": JsCode(color_function),       # 调整柱子颜色渐变
                'shadowBlur': 8,   # 光影大小
                "barBorderRadius": [100, 100, 100, 100],  # 调整柱子圆角弧度
                "shadowColor": "#E9B7D3", # 调整阴影颜色
                'shadowOffsetY': 6,
                'shadowOffsetX': 6,  # 偏移量
            }
        }
    )
    bar.set_global_opts(
    # 标题设置
    title_opts=opts.TitleOpts(
        title='每月各产品类别销售额top榜单', # 主标题
        subtitle='', # 副标题
        pos_left='center',  # 标题展示位置
        title_textstyle_opts=dict(color='#5A3147'), # 设置标题字体颜色
        subtitle_textstyle_opts=dict(color='#5A3147')
    ),
    legend_opts=opts.LegendOpts(
        is_show=True, # 是否显示图例
        pos_left='right', # 图例显示位置
        pos_top='3%',  #图例距离顶部的距离
        orient='vertical',  # 图例水平布局
        textstyle_opts=opts.TextStyleOpts(
            color='#5A3147',  # 颜色
            font_size='13',   # 字体大小
            font_weight='bolder',   # 加粗
    ),
    ),
    tooltip_opts=opts.TooltipOpts(
        is_show=True,  # 是否使用提示框
        trigger='axis',  # 触发类型
        is_show_content = True,
        trigger_on='mousemove|click',  # 触发条件，点击或者悬停均可出发
        axis_pointer_type='cross',  # 指示器类型，鼠标移动到图表区可以查看效果
        # formatter = '{a}<br>{b}:{c}人'  # 文本内容
    ),
    yaxis_opts=opts.AxisOpts(
        is_show=True,
        splitline_opts=opts.SplitLineOpts(is_show=False), # 分割线
        axistick_opts=opts.AxisTickOpts(is_show=False), # 刻度不显示
        axislabel_opts=opts.LabelOpts(  # 坐标轴标签配置
            font_size=13,  # 字体大小
            font_weight='bolder' # 字重
        ),
    ),   # 关闭Y轴显示
    xaxis_opts=opts.AxisOpts(
        boundary_gap=True,    # 两边不显示间隔
        axistick_opts=opts.AxisTickOpts(is_show=True),  # 刻度不显示
        splitline_opts=opts.SplitLineOpts(is_show=False),  # 分割线不显示
        axisline_opts=opts.AxisLineOpts(is_show=True),  # 轴不显示
        axislabel_opts=opts.LabelOpts(  # 坐标轴标签配置
            font_size=13,  # 字体大小
            font_weight='bolder' # 字重
            ),
        ),
    )

    t2.add(bar, day)

t2.render_notebook()
pro_category = {
    'ZMDC':['COA','ISR','Femur','HCC','ACC','SIS','Silicosis','TCGA','AR','SAH'],
    #'ZMDC':['主动脉弓狭窄','动脉狭窄','股骨假体周围骨折','肝肿瘤','慢性丹囊炎','矽肺','膝关节滑膜囊肿','骨恶性肿瘤','主动脉瓣关闭不全','蛛网膜下腔出血'],
    '一级医院':[47772.13,24344.24,22613.36,21825.21,21037.6,20392.86,19665.33,19615.65,19194.55,18373.56],
    '二级医院':[49908.15,25633.44,23065.43,22134.34,20056.33,21003.2,19003.55,19522.67,18977.77,19004.77],
}
pro_category = pd.DataFrame(pro_category,index=['1','2','3','4','5','6','7','8','9','10'])
pro_category

def echarts_bar(x,y,y2,title = '主标题',subtitle = '副标题',label = '图例',label2 = '图例2',color='color'):
    """
    x: 函数传入x轴标签数据
    y：函数传入y轴数据
    title：主标题
    subtitle：副标题
    label：图例
    """
    bar = Bar(
            init_opts=opts.InitOpts(
            bg_color='#3333cc',  # 设置背景颜色
            theme='dark',         # 设置主题
            width='900px',     # 设置图的宽度
            height='600px'     # 设置图的高度
        )
    )
    bar.add_xaxis(x)
    bar.add_yaxis(label,y,
        label_opts=opts.LabelOpts(is_show=True) # 是否显示数据
        ,category_gap="60%" # 柱子宽度设置
        ,yaxis_index=0
        ) 
    bar.add_yaxis(label2,y2,
        label_opts=opts.LabelOpts(is_show=True) # 是否显示数据
        ,category_gap="60%" # 柱子宽度设置
        ,yaxis_index=1
    )
    bar.set_series_opts( # 自定义图表样式
        label_opts=opts.LabelOpts(
            is_show=True,
            position='top', # position 标签的位置 可选 'top'，'left'，'right'，'bottom'，'inside'，'insideLeft'，'insideRight'
            font_size=15,
            color= 'white',
            font_weight = 'bolder',  # font_weight 文字字体的粗细  'normal'，'bold'，'bolder'，'lighter'
            font_style = 'oblique',  # font_style 文字字体的风格，可选 'normal'，'italic'，'oblique'
            ), 
        itemstyle_opts={  
            "normal": {
                "color": color,       # 调整柱子颜色渐变
                'shadowBlur': 15,   # 光影大小
                "barBorderRadius": [100, 100, 100, 100],  # 调整柱子圆角弧度
                "shadowColor": "#0EEEF9", # 调整阴影颜色
                'shadowOffsetY': 10,
                'shadowOffsetX': 10,  # 偏移量
            }
        }
    )
    bar.set_global_opts(
        # 标题设置
        title_opts=opts.TitleOpts(
            title=title, # 主标题
            subtitle=subtitle, # 副标题
            pos_left='center',  # 标题展示位置
            title_textstyle_opts=dict(color='#fff') # 设置标题字体颜色
        ),
        # 图例设置
        legend_opts=opts.LegendOpts(
            is_show=True, # 是否显示图例
            pos_bottom='bottom',
            orient='horizontal'  # 图例水平布局
        ),
        tooltip_opts=opts.TooltipOpts(
            is_show=True,  # 是否使用提示框
            trigger='axis',  # 触发类型
            is_show_content = True,
            trigger_on='mousemove|click',  # 触发条件，点击或者悬停均可出发
            axis_pointer_type='cross',  # 指示器类型，鼠标移动到图表区可以查看效果
        ),
        yaxis_opts=opts.AxisOpts(
            is_show=True,
            splitline_opts=opts.SplitLineOpts(is_show=False), # 分割线
            axistick_opts=opts.AxisTickOpts(is_show=False), # 刻度不显示
            axislabel_opts=opts.LabelOpts(  # 坐标轴标签配置
                font_size=13,  # 字体大小
                font_weight='bolder' # 字重
            ),
        ),   # 关闭Y轴显示
        xaxis_opts=opts.AxisOpts(
            boundary_gap=True,    # 两边不显示间隔
            axistick_opts=opts.AxisTickOpts(is_show=True),  # 刻度不显示
            splitline_opts=opts.SplitLineOpts(is_show=False),  # 分割线不显示
            axisline_opts=opts.AxisLineOpts(is_show=True),  # 轴不显示
            axislabel_opts=opts.LabelOpts(  # 坐标轴标签配置
                font_size=13,  # 字体大小
                font_weight='bolder' # 字重
            ),
        ),
    )
    bar.extend_axis(yaxis=opts.AxisOpts())
    return bar.render_notebook()

color = {
       'type': 'linear',
        'x': 0,
        'y': 0,
        'y2': 0,
        'x2': 1,
        'colorStops': [
            {'offset': 0, 'color': 'rgba(0, 244, 255, 0.8)' }, 
            {'offset': 1, 'color': 'rgba(0, 77, 167, 0.8)'}],
        'global': False 
    }
echarts_bar(pro_category['ZMDC'].tolist(), pro_category['一级医院'].tolist(),
            pro_category['二级医院'].tolist(), title='不同医院费用对比', subtitle='花费金额对比柱状图',
            label='一级医院', label2='二级医院', color=color)

shuju = data['JGDJ'].value_counts()
shuju

from pyecharts.charts import *
from pyecharts import options as opts
'''饼图'''
L1 = ["社区医疗","二级医院","三级医院","一级医院"]
num = [5837,5029,2974,2725]
C = Pie()
C.add("饼图",[list(z) for z in zip(L1,num)])
C.set_global_opts(title_opts=opts.TitleOpts(title="饼图"))
#C.set_series_opts(label_opts=opts.TitleOpts(formatter="{b}:{c}"))
C.render_notebook()

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

df1 = data['ZDMC'].value_counts()
df0  = df1.head(20)

# color={
#        'type': 'linear',
#         'x': 0,
#         'y': 1,
#         'x2': 0,
#         'y2': 0,
#         'colorStops': [
#             {'offset': 0, 'color': 'black' }, 
#             {'offset': 1, 'color': 'orange'}],
#         'global': False 
#     }
c1 = (
    Pie()
    .add('test', [list(z) for z in zip(df0.index.values.tolist(), df0.values.tolist())],
         radius=['30%', '100%'],
         center=['50%', '60%'],
         rosetype='area',
         )
    .set_global_opts(title_opts=opts.TitleOpts(title='地区景点数量'),
                     legend_opts=opts.LegendOpts(is_show=False),
                     toolbox_opts=opts.ToolboxOpts()
                    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12,
                                               formatter='{b}: {c}', font_style='italic',
                                               font_weight='bold', font_family='Microsoft YaHei'
                                               ),
#                     itemstyle_opts=opts.ItemStyleOpts(color=color)
                    )
)
c1.render_notebook()

dff = data['RYLB'].value_counts()
dff

from pyecharts.charts import *
from pyecharts import options as opts
'''圆环图'''
L1 = ["居民","退休类型1","退休类型2","在职类型1","在职类型2","离休"]
num = [10104,1510,2984,1458,445,64]
C = Pie()
'''radius调节大小'''
C.add("圆环图",[list(z) for z in zip(L1,num)],radius=["45%","75%"])
C.set_global_opts(title_opts=opts.TitleOpts(title="圆环图"),legend_opts=opts.LegendOpts(orient="vertical",pos_top="2%",pos_left="5%"))
C.render_notebook()

dfff = data['XB'].value_counts()
dfff

import pyecharts.options as opts
from pyecharts.charts import Pie

"""

"""

inner_x_data = ["男", "女"]
inner_y_data = [8551 , 8012]
inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]

outer_x_data = ["社区医疗","二级医院","三级医院","一级医院"]
outer_y_data = [5837,5029,2974,2725]
outer_data_pair = [list(z) for z in zip(outer_x_data, outer_y_data)]

c = (
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="涨跌情况",
        data_pair=inner_data_pair,
        radius=[0, "30%"],
        label_opts=opts.LabelOpts(position="inner"),
    )
    .add(
        series_name="涨跌情况",
        radius=["40%", "55%"],
        data_pair=outer_data_pair,
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"))
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
    .render_notebook()
)

c

dffff = data['YLLB'].value_counts()
dffff

from pyecharts import options as opts
from pyecharts.charts import PictorialBar
from pyecharts.globals import SymbolType

location = ['门诊慢性病' ,'普通住院' , '普通门诊',' 转省外住院特殊疾病门诊 ', '转省内住院无责任人意外伤害' ,'生育住院'    , 
            '转省外门诊慢性病' ,'转省内门诊慢性病'  ,'大病购药' ,'机关事业单位生育住院' ,'住院前急诊' ,'转省平台住院','单病种住院']
values = [7245, 3222 ,2117, 1334 ,1023, 490 , 423 ,387 ,194, 68 ,36,  13 , 10 , 2,1]

c = (
    PictorialBar()
    .add_xaxis(location)
    .add_yaxis(
        "",
        values,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=18,
        symbol_repeat="fixed",
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol=SymbolType.ROUND_RECT,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="医疗类别"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
    )
    .render_notebook()
    #.render("pictorialbar_base.html")
)
c


