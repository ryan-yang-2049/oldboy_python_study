import os
import re
import requests
from lxml import etree
from YDM_test import YDMHttp

# 该函数调用了打码平台的相关接口对指定的验证码图片进行识别，返回图片上的数据值
def getCode(codeImg):
	# 云打码平台普通用户的用户名
	username = 'ryan_cherry'
	# 密码
	password = 'Ryan!@99'
	# 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
	appid = 6160    # 软件代码
	# 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
	appkey = 'cc2b21d94c423a2a2b24f76c0945bca7'
	# 图片文件
	filename = codeImg
	# 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
	codetype = 3000
	# 超时时间，秒
	timeout = 20
	# 检查
	if (username == 'username'):
		print('请设置好相关参数再测试')
	else:
		# 初始化
		yundama = YDMHttp(username, password, appid, appkey)
		# 登陆云打码
		uid = yundama.login();
		print('uid: %s' % uid)
		# 查询余额
		balance = yundama.balance();
		print('balance: %s' % balance)
		# 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
		cid, result = yundama.decode(filename, codetype, timeout);
		print('cid: %s, result: %s' % (cid, result))
		return result
######################################################################


url = 'https://www.douban.com/accounts/login?source=movie'

# 自定义请求头信息
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}

page_text = requests.get(url=url,headers=headers).text
# 解析验证码
tree = etree.HTML(page_text)
code_img_url = tree.xpath('//*[@id="captcha_image"]/@src')[0]
print(code_img_url)
# 获取 captcha-id  src="https://www.douban.com/misc/captcha?id=xZHOusVpvtv07FLkgozgF0fu:en&amp;size=s"
captcha_id = re.findall('.*?id=(.*?)&.*?',code_img_url)
# captcha_id = re.findall('<img id="captcha_image".*?id=(.*?)&amp.*?>',page_text,re.S)
print(captcha_id)
# 获取了验证码图片对应的二进制数据值
code_img = requests.get(url=code_img_url,headers=headers).content
with open('./code_img.png','wb') as fp:
	fp.write(code_img)

# 普通用户：ryan_cherry  Ryan!@99
# 开发者用户 ryan_cherry2 Ryan!@99

if os.path.exists('./code_img.png'):
	# 获取图片上的验证码
	codeText = getCode('./code_img.png')
	print(codeText)

# 进行登陆操作

login_url = 'https://accounts.douban.com/login'
# 2.封装post的请求
data = {
	'source':'movie',
	'redir':'https://movie.douban.com/',
	'form_email':'461580544@qq.com',
	'form_password':'Ryan!@99',
	'captcha-solution': codeText,
	'captcha-id':captcha_id[0],
	'login':'登录'
}
print(captcha_id)
login_text = requests.post(url=login_url,data=data,headers=headers).text
with open('./login.html','w',encoding='utf-8') as fp:
	fp.write(login_text)

