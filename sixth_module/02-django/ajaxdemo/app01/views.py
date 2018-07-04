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



def file_put(request):
	if request.method == "POST":
		print("POST",request.POST)
		print(request.FILES)
		file_obj = request.FILES.get("avatat")
		with open(file_obj.name,'wb') as f:
			for line in file_obj:
				f.write(line)
		return HttpResponse("OK")
	return render(request,"test.html")



'''
请求首行
请求头

····
ContentType：urlencoded
请求体 {"a":"1","b":"2"}                    (a=1&b=2&c=3)



'''







