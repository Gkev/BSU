# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def index(request):
	return render(request, 'blogs/index.html')


def new(request):
	return HttpResponse("New blog")


def create(request):
	return redirect('/')



def show(request, bnum):
	
	return HttpResponse("hello" + bnum)


def edit(request, enum):
	return HttpResponse("Edit this number" + enum)



def destory(request, dnum):
	return redirect(request,'/blogs')
