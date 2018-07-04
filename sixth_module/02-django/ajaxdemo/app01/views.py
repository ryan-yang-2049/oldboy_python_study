from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
	return render(request,"index.html")



def test_ajax(request):
	print(request.GET)  # <QueryDict: {'a': ['1'], 'b': ['2']}>
	return HttpResponse("hello ajax")


def cal(request):
	print(request.POST)
	n1 = request.POST.get("n1")
	n2 = request.POST.get("n2")
	res = int(n1) + int(n2)
	return HttpResponse(res)


from app01.models import User
import json
def login(request):
	print(request.POST)
	user = request.POST.get("user")
	pwd = request.POST.get("pwd")

	user_info = User.objects.filter(name=user,pwd=pwd).first()
	res = {"user":None,"msg":None}
	if user_info:
		res["user"] = user_info.name
	else:
		res["msg"]="username or password wrong"


	return HttpResponse(json.dumps(res))



# def file_put(request):
# 	if request.method == "POST":
# 		print("body:",request.body)   # 请求报文中的请求体 ,JSON 的字符串
# 		print("path",request.path)  # path /file_put/
# 		# 只有在 ContentType== urlencoded 时, request.POST 才会有数据
# 		print("POST",request.POST)    # POST <QueryDict: {'user': ['cherry']}>
# 		# print(request.FILES)   # <MultiValueDict: {'avatat': [<InMemoryUploadedFile: 13.jpg (image/jpeg)>]}>
# 		# file_obj = request.FILES.get("avatat")
# 		# with open(file_obj.name,'wb') as f:
# 		# 	for line in file_obj:
# 		# 		f.write(line)
# 		return HttpResponse("OK")
# 	return render(request,"test.html")

def file_put(request):
	if request.method == "POST":
		print("body:",request.body)   #res:body: b'{"a":1,"b":3}'  请求报文中的请求体 ,JSON 的字符串
		# 只有在 ContentType== urlencoded 时, request.POST 才会有数据
		print("POST",request.POST)   # POST <QueryDict: {}>
		return HttpResponse("OK")
	return render(request,"test.html")


'''
请求首行
请求头

····
ContentType：urlencoded
请求体 {"a":"1","b":"2"}                    (a=1&b=2&c=3)



'''







