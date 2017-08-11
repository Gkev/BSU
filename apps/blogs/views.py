# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


# Create your views here.

def index(request):
	return HttpResponse("Start Here")


def create(request, words):
	return HttpResponse("New blogs" )



def show(request, name):
	return HttpResponse("Create new blog" + nblogs)
