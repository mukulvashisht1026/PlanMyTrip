from django.shortcuts import render
from django.http import HttpResponse
import csv
import pandas as pd
from random import randint
import numpy as np
from math import sqrt
import os
import datetime
import requests 
import json
from django.contrib.auth.decorators import login_required
# from .data import users
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path_to_file = BASE_DIR +'/data/users.csv'
users = pd.read_csv(BASE_DIR + '/data/users.csv')
hill_data = pd.read_csv(BASE_DIR + '/data/finaldraftpart2.csv')

col = ['userId', 'age', 'placeid', 'expenses', 'rating','noofdays', 'numberofpeople','dateofvisit','haschildren?']
# df = pd.read_csv('Detail_Of_Places.csv')
# df['budget'] = df['budget'].fillna(df['budget'].mean())
# newdf = df[['name','budget']]
# Create your views here.

@login_required
def index(request):

	return render(request,'HomePage/HomePage.html',{})


@login_required
def GetPlaces(request):

	print(request.GET)
	l = []
	l.append(int(request.GET.get('age',0)))
	l.append(int(request.GET.get('budget',0))/1000)

	l.append(int(request.GET.get('no_of_days',0)))
	l.append(int(request.GET.get('no_of_people',0)))
	l.append(int(datetime.datetime.strptime(request.GET.get('start_date',0), "%Y-%m-%d").month))

	if (request.GET.get('child') == None):
		l.append(0)
	else:
		l.append(1)

	l1 = l
	data = np.array(users)
	helper = []
	for row in data:
	    ans = 0
	    ans += (int(row[0])-l1[0])**2 
	    ans += (int(row[2])-l1[1])**2
	    ans += (int(row[3])-l1[2])**2
	    ans += (int(row[4])-l1[3])**2
	    ans += (int(row[5])-l1[4])**2
	    ans += (int(row[6])-l1[5])**2
	    
	    ans = sqrt(ans)
	    helper.append([ans,row])

	helper.sort(key=lambda x:x[0])

	fav_places = set()#set = fav places
	for i in helper[0:15]:
	    fav_places.add(int(i[1][1]))
	
	context = {}
	hillData = np.array(hill_data)
	count =1
	context['placeslist'] =[]
	months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
	for i in fav_places:
		print(i)

		mydict = {
		'srn' : count,
		'id' : hillData[i][0],
		'name' : hillData[i][1],
		'rating' : hillData[i][2],
		'link' : hillData[i][3],
		'description' : hillData[i][6],
		'price' : float(hillData[i][4]),
		'start_month' : months[int(hillData[i][8]) - 1],
		'end_month' : months[int(hillData[i][9])-1],
		'place_code' : hillData[i][7],
		'type' : hillData[i][10]
		} 
		# print(mydict['from'])
		context['placeslist'].append(mydict)
		# 'from' : request.GET.get('from')
		context['from'] = request.GET.get('from')
		count 	= count + 1
	# print(context['from'])
	# print(context)
	return render(request, 'HomePage/cards.html', context)



def viewmore(request,id):
	if request.method == 'GET':
		detail_data = pd.read_csv(BASE_DIR + '/data/DetailHillStations.csv')
		df = np.array(detail_data)
		inside_places = []
		print(type(id))
		for i in df:
			# print(i[3])
			if(i[1] == id):
				mydict = {
					"insid_Id" : i[0],
					"name" : i[2],
					"image_link" : i[3],
					# "name" : i[i][2],
					"rating" : i[4],
					"description" : i[6]

				}
				inside_places.append(mydict)
		hillData = np.array(hill_data)
		# print(request.GET.get('from'),"sdjkhfkajsdhfksdfhkjhksdhfjs")
		source = request.GET.get('from')
		destination = hillData[id][1]
		# print(source,"  --  ",destination)
		url = 'https://www.holidify.com/rest/utility/getDirections.hdfy'
		headers = {'sourceName':source,
		           'destinationName':destination,
		          }


		r =requests.get(url,params=headers)
		trav = json.loads(r.content)
		c = 0
		title = {}
		duration ={}
		price = {}
		routeSegment = {}
		sab = []
		for i in trav:
			c = c+1
			print(i)
			temp = {}
			temp["title"] = i["title"]
			temp["duration"] = round(int(i["duration"])/60,2)
			if i["price"] == None:
				temp["price"] = int(0)
			else:
				temp["price"] = int(i["price"])
			temp["routeSegment"] = []
			print("hello world")
			for j in i["routeSegments"]:
				temp2 = {}
				temp2["sname"] = j["sName"]
				temp2["tname"] = j["tName"]
				temp2["vehicle"] = j["vehicle"]
				temp2["price"] = j["price"]
				temp2["duration"] = round(int(j["duration"])/60,2)
				temp2["ismajor"] = j["isMajor"]
				temp["routeSegment"].append(temp2)
				print(temp2)

			# print(i["routeSegments"])
			sab.append(temp)
			# title.append(i['title'])
			# duration.append(i['duration'])
			# price.append(i['price'])
			# routeSegment.append(i['routeSegments'])
		# print(title)


		context = {
			"id" : id,
			"inside_places" : inside_places,
			"travelling" : sab,
			"destination" : destination
			}



		return render(request, 'HomePage/detail.html', context)

'''
# BUILDING A API FOR DIRECTION
import requests
url = 'https://www.holidify.com/rest/utility/getDirections.hdfy'
headers = {'sourceName':'manali',
           'destinationName':'Solang Valley',
          }
r =requests.get(url,params=headers)

'''