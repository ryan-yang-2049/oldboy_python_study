# -*- coding: utf-8 -*-

# __title__ = '02.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.04.25'


import plotly.offline as pltoff
import plotly.graph_objs as go


def bar_charts(name="index.html"):
	# dataset = {'x': ['user'],
	#            'y1': [35]}
	dataset = {'"223.104.212.209"': 2, '"101.227.139.164"': 1, '"101.227.139.178"': 1, '"180.167.94.50"': 47, '"101.227.139.161"': 1,'"101.227.139.1"': 1, '"101.27.139.164"': 1,'"10.227.139.164"': 1,'"11.227.139.164"': 1,'"223.104.212.20"': 3}
	data_g = []
	ip_li = [x for x in dataset]

	tr_y1 = go.Bar(
		x=ip_li,
		y=[dataset[y] for y in ip_li],
		marker=dict(
			color=["#FF0000", "#00FF00"],
		)
	)
	data_g.append(tr_y1)

	layout = go.Layout(title="51达欧盛典用户访问图",
	                   xaxis={'title': '用户IP地址'}, yaxis={'title': '用户连接次数'})
	fig = go.Figure(data=data_g, layout=layout)
	pltoff.plot(fig, filename=name)


if __name__ == '__main__':
	bar_charts()







