import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Range1d, DatetimeTickFormatter
from bokeh.models.tools import HoverTool


df = pd.read_csv('/Users/lancebiddle/CodeYou/Capstone Project/Harvest Data/Data Cleaned/Merged/Harvest_Data_Merged.csv')

x = df.iloc[0:, 0]
y = df.iloc[0:, 1]
title = df.head

print(title)

p = figure(x_range=x, title="Harvest Results", x_axis_label="Dates", y_axis_label="Harvest Amount")
p.vbar(x=x, top=y, width=0.9, color= 'green')
p.xaxis.major_label_orientation = "vertical"
text_font = 'helvetica'
text_font_style = 'normal'
text_color = 'red'
show(p)
