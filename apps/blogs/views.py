# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def index(request):
	return HttpResponse("Start Here")


def new(request):
	return HttpResponse("New blog")


def create(request, nblogs):
	return redirect('/blogs')



def show(request, bnum):
	print bnum
	return HttpResponse("hello" + bnum)


def edit(request, enum):
	return HttpResponse("Edit this number" + enum)



def destory(request, dnum):
	return redirect('/blogs')
