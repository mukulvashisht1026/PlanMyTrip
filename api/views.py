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
		count =0
		for row in data:
			if(count == 0):
				count =1
				continue
			if(row[4]==''):

				row[4] = 0.0
			# print(type(int(float(row[4]))))
			# print(row[4])


			if(float(row[4])<= float(Budget)):
				context['list_of_places'].append({
					"nameOfPlace" : row[1],
					"linkOfImage" : row[2],
					"description" : row[3],
					"budget"	  : row[4]
					}) 

	return HttpResponse(json.dumps(context),content_type="application/json")