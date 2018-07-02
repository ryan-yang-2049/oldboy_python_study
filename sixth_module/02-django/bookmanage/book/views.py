from django.shortcuts import render

# Create your views here.
from book.models import *


def add_book(request):

	publish_list = Publish.objects.all()
	author_list = Author.objects.all()

	return render(request,"addbook.html",locals())