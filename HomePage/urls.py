from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
	path('',views.index),
	path('getplaces/',views.GetPlaces),	
	path('viewmore/<int:id>/', views.viewmore, name='myname')
]
