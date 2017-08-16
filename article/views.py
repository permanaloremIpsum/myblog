# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myview(request):
	return HttpResponse('<h1>This is my view</h1>')
def hello_world(request):
	return HttpResponse('Hello World')
def nama(request, nama_saya, umur):
	return HttpResponse('Nama saya %s, umur saya adalah %s tahun' % (nama_saya, umur))

def home(request):
	return render(request, 'index.html')