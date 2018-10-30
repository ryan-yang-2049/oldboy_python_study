from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def index(request):

	return  render(request,"index.html")


def test_ajax(request):

	print(request.GET)


	return HttpResponse("hello Ajax!")

def cal(request):

	n1 = request.GET.get("n1")
	n2 = request.GET.get("n2")
	if n1.isdigit()  and n2.isdigit():
		res = int(n1) + int(n2)
		return HttpResponse(res)
	else:
		return HttpResponse("must be integer")


from app01.models import User
import json
def login(request):
	if request.method == "GET":
		return render(request,"login.html")
	print(request.POST)
	user = request.POST.get("user")
	pwd = request.POST.get("passwd")
	user_info = User.objects.filter(name=user, pwd=pwd).first()
	res = {"user": None, "msg": None}
	if user_info:
		res["user"] = user_info.name
	else:
		res["msg"] = "username or password wrong"
	return HttpResponse(json.dumps(res))


def file_put(request):

	if request.method == "POST":
		print("request.POST",request.POST) # 只有 ContentType== urlencoded 的时候 request.POST 才有值

		print("request.body==>",request.body)
		file_obj = request.FILES.get("avatar02")
		with open(file_obj.name, 'wb') as f:
			for line in file_obj:
				f.write(line)
		return HttpResponse("OK")


	return render(request,"file_put.html")
