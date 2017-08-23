# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Category, Post

# Create your views here.
def myview(request):
	return HttpResponse('<h1>This is my view</h1>')
def hello_world(request):
	return HttpResponse('Hello World')
def nama(request, nama_saya, umur):
	return HttpResponse('Nama saya %s, umur saya adalah %s tahun' % (nama_saya, umur))

def home(request):
	categories = Category.objects.all()
	posting = Post.objects.all().order_by('-created_on')[:3]
	data = {
		'categories': categories,
		'posting' : posting,
	}
	return render(request, 'index.html', data)

def single(request, slug):
	categories = Category.objects.all()
	posting = Post.objects.get(slug=slug)
	data = {
		'categories': categories,
		'posting' : posting,
	}
	return render(request, 'single.html', data)

def cat(request):
	categories = Category.objects.all()
	data = {
		'categories': categories,
	}
	return render(request, 'category.html', data)

def list_cat(request, id):
	catlist = Category.objects.get(id=id)
	categories = Category.objects.all()
	post = Post.objects.filter(category=catlist)
	data = {
		'catlist': catlist,
		'categories': categories,
		'post': post,
	}
	return render(request, 'list_cat.html', data)
