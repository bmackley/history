from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from django.conf import settings
import decimal, datetime
from django.contrib.auth import logout
from . import templater

def process_request(request):
	if request.method=='GET':
		query = request.GET.get('search')
		if query is None:
			search = False
			

	tvars= {

	}
	return templater.render_to_response(request, 'index.html', tvars)