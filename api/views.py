from django.shortcuts import render
from django.http import HttpResponse
import os 
# Create your views here.

import csv
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
def index(request,):
	Budget = request.GET['Budget']
	path_to_file = BASE_DIR +'/data/Detail_Of_Places.csv'
	with open(path_to_file,'rt')as f:
		data = csv.reader(f)
		context = {
		'list_of_places': [] 
		}
		for row in data:
			if(row[4]<=Budget):
				context['list_of_places'].append(row) 

	return HttpResponse(json.dumps(context),content_type="application/json")