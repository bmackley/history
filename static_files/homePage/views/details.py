from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m 
from django.db.models import Q
from . import templater

def process_request(request):
	product = m.catalogProduct.objects.get(id=request.urlparams[0])

	tvars = {
		'product': product,
	}
	return templater.render_to_response(request, 'details.html', tvars)