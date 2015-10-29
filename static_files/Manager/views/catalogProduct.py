from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m 
from . import templater

def process_request(request):
	'''Shows the List of Stores'''
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/Manager/login')
	
	if request.urlparams[0] == 'delete':
		catalogProduct = m.catalogProduct.objects.get(id=request.urlparams[1])
		catalogProduct.is_active = False 
		catalogProduct.save()

	catalogProduct = m.catalogProduct.objects.exclude(active=False)
	
	tvars = {
		'catalogProduct' : catalogProduct,
	}
	return templater.render_to_response(request, 'catalogProduct.html', tvars)

