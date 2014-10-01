from django.shortcuts import render
from django.http import HttpResponse
import json
from hellodjango.models import Hello


def home(request):
	return render(request, "home.html", {})


def GetUserLatestInfo(request):
	hellos = Hello.objects.all()
	hello_list = []
	for hello in hellos:
		hello_dict = {}
		hello_dict['name'] = hello.name
		hello_dict['description'] = hello.description
		hello_list.append(hello_dict)

	hello_json = json.dumps(hello_list)
	return HttpResponse(hello_json)

