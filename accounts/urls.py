from django.urls import path,include
from .views import *

urlpatterns = [
	path('signup/',signup,name='signup'),
	path('login/',login,name = 'login'),
	path('logout/',logout,name = 'logout'),

	#path('signup_1/',signup_1,name='signup_1'),

]
