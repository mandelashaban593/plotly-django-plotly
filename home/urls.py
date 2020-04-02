from django.urls import path
from . import views

from django.conf.urls import url, include
from django.contrib import admin

from  home.views import home
from plotlydjango.settings import *






urlpatterns =[
	url('',home, name='home')

	]