import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Timeline
import random

data=pd.read_excel('地区生产总值(亿元).xlsx',sheet_name='Sheet1',index_col=0)
x=list(data.columns)
y=data.values
year=list(data.index)

# 随机生成31种颜色
get_colors=lambda n:list(map(lambda i:"#"+"%06x"%random.randint(0,0xFFFFFF),range(len(x))))
one_color=get_colors(len(x))

timeline=Timeline()
for i in range(len(data)):
    xy=list(zip(x,y[i],one_color)) # 给每个地区匹配一种颜色
    xy.sort(key=lambda x:x[1],reverse=False)
    xy=xy[-10:]
    bar=(
        Bar()
        .add_xaxis(xaxis_data=[i[0] for i in xy])
        .add_yaxis(series_name=str(2002+i)+'年地区生产总值',y_axis=[i[1] for i in xy],color=[i[2] for i in xy])
        .reversal_axis()
        .set_global_opts(title_opts=opts.TitleOpts(title='地区生产总值排行榜（%s年）'%(2002+i),subtitle='单位：亿元',pos_left='center',pos_top='top'),
                         legend_opts=opts.LegendOpts(is_show=False),
                         visualmap_opts=opts.VisualMapOpts(is_show=False,range_color=[i[2] for i in xy],min_=0,max_=10))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True,position='right',color='red'))
        )
    timeline.add(bar,year[i]).add_schema(is_auto_play=True)
timeline.render('动态排行榜二.html')
