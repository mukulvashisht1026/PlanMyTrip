from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

	return render(request,'HomePage/Base.html',{})

def GetPlaces(request):
	# print(request.GET)
	l = []
	l.append(request.GET['no_of_days'])
	l.append(request.GET['age'])
	l.append(request.GET['budget'])
	l.append(request.GET['from'])
	l.append(request.GET['start_date'])
	l.append(request.GET['no_of_people'])
	if (request.GET.get('child') == None):
		l.append(False)
	else:
		l.append(request.GET.get('child'))


	return HttpResponse(l)