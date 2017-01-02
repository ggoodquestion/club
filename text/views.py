# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from text.models import AbouTxt ,DecTxt ,ClassTxt ,Worker

# Create your views here.

def about(request):
	aboutxt = AbouTxt.objects.all()
	return render_to_response('about.html' , locals())

def class1(request):
	classtxt = ClassTxt.objects.all()
	return render_to_response('class.html' , locals())

def declare(request):
	dectxt = DecTxt.objects.all()
	return render_to_response('declare.html' , locals())

def index(request):
	worker = Worker.objects.all()
	return render_to_response('index.html', RequestContext(request, locals()))