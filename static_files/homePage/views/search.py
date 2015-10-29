from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m 
from django.db.models import Q
from . import templater

def process_request(request):
	'''Shows the List of Groups'''
	if request.method == 'GET':
		query = request.GET.get('search')
	if query is None:
		search = False
		Objects = ""
		results = False
	else:
		search = True
		query = query.lower()
		Objects = m.Group.objects.filter(Q(lgroupName__contains= query) | Q(zipcode__contains=query)| Q(lcity__contains=query))
		#Objects = m.catalogProduct.objects.all()
		count = 0
		for number in Objects:
			count+=1
		if count > 0:
			results=True
		else:
			results=False
	tvars = {
		'search': search,
		'Objects': Objects,
		'results': results,
	}
	return templater.render_to_response(request, 'search.html', tvars)