# -*- coding: utf-8 -*-

# __title__ = 'validCode.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.07.10'


import random


def get_random_color():
	return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def get_valid_code_img(request):


	# 方式一：原始图片就有的
	# with open("lufei.jpg","rb") as f:
	# 	data = f.read()

	# 方式二：磁盘中
	# from PIL import Image
	# img = Image.new("RGB",(260,35),color=get_random_color())   #RGB：一种模式
	#
	# with open("validCode.png","wb") as f:
	# 	img.save(f,"png")
	#
	# with open("validCode.png","rb") as f:
	# 	data = f.read()

	# 方式三：内存中
	# from PIL import Image
	# from io import BytesIO
	# img = Image.new("RGB",(260,35),color=get_random_color())   #RGB：一种模式
	# f=BytesIO()  #内存句柄
	# img.save(f,"png")
	# data = f.getvalue()

	# 方式四：
	from PIL import Image, ImageDraw, ImageFont
	from io import BytesIO
	# 画板
	img = Image.new("RGB", (260, 35), color=get_random_color())  # RGB：一种模式

	# 画笔
	draw = ImageDraw.Draw(img)
	# draw.text(): 写文字 draw.line(): 画线  draw.point() : 画点
	# 字体对象
	kumo_font = ImageFont.truetype("static/font/kumo.ttf", size=30)

	# 随机验证码
	valid_code_str = ""
	for i in range(5):
		random_num = str(random.randint(0, 9))
		random_low_alpha = chr(random.randint(97, 122))
		random_upper_alpha = chr(random.randint(65, 90))
		random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
		draw.text((i * 50 + 20, 5), random_char, get_random_color(), font=kumo_font)

		# 保存验证码字符串
		valid_code_str += random_char

	# 噪点 噪线
	# width = 260
	# height = 35
	# for i in range(5):
	# 	x1 = random.randint(0, width)
	# 	x2 = random.randint(0, width)
	# 	y1 = random.randint(0, height)
	# 	y2 = random.randint(0, height)
	# 	draw.line((x1, y1, x2, y2), fill=get_random_color())
	#
	# for i in range(50):
	# 	draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
	# 	x = random.randint(0, width)
	# 	y = random.randint(0, height)
	# 	draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

	print(valid_code_str)
	request.session["valid_code_str"] = valid_code_str
	'''
	1.生成随机字符串
	2.COOKIE{"session":随机字符串}
	3 django-session
		session-key  session-data
		随机字符串   {"valid_code_str":"验证码"}

	'''
	f = BytesIO()  # 内存句柄
	img.save(f, "png")
	data = f.getvalue()

	return data


# 滑动验证码  social-auth-app-django



