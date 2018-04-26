# -*- coding: utf-8 -*-

# __title__ = 'chart_view.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.04.25'



import plotly.offline as pltoff
import plotly.graph_objs as go


def bar_charts(name="bar_charts.html"):
	dataset = {'x': ['man', 'woman'],
	           'y1': [35, 26],
	           'y2': [33, 30]}
	data_g = []
	tr_y1 = go.Bar(
		x=dataset['x'],
		y=dataset['y1'],
		name='2016'

	)
	data_g.append(tr_y1)

	tr_y2 = go.Bar(
		x=dataset['x'],
		y=dataset['y2'],
		name='2017'

	)
	data_g.append(tr_y2)
	layout = go.Layout(title="bar charts",
	                   xaxis={'title': 'x'}, yaxis={'title': 'value'})
	fig = go.Figure(data=data_g, layout=layout)
	pltoff.plot(fig, filename=name)


if __name__ == '__main__':
	bar_charts()







