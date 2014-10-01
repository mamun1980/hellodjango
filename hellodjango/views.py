from django.shortcuts import render
from django.http import HttpResponse
import json
from hellodjango.models import Hello
import datetime

def home(request):
	return render(request, "home.html", {})


def GetUserLatestInfo(request):
	mynow = datetime.datetime.now()
	thirtysec = datetime.timedelta(seconds=25)
	before_thirty = mynow - thirtysec
	hellos = Hello.objects.all().order_by("name")

	# hellos = Hello.objects.filter(modified_at__gte=before_thirty, created_at__gte=before_thirty)
	hello_list = []
	for hello in hellos:
		hello_dict = {}
		hello_dict['name'] = hello.name
		hello_dict['description'] = hello.description
		hello_list.append(hello_dict)

	hello_json = json.dumps(hello_list)
	return HttpResponse(hello_json)

