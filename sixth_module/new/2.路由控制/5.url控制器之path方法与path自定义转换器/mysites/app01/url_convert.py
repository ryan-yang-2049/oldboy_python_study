



class MonConvert(object):
	# 必须叫 regex
	regex = "[0]{1}[1-9]{1}|[1][0-2]{1}"

	def to_python(self,value):
		return int(value)

	def to_url(self,value):     # 反向解析
		return '$04d' % value
