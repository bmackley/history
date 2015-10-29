from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m 
from . import templater

def process_request(request):
	'''Shows the List of Stores'''
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/Manager/login')
	group = m.Group.objects.get[id=request.urlparams[0]]
	if group.administrator != request.user:
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/Manager/groupUsers' + str(group.id))
	if request.urlparams[0] == 'delete':
		groups = m.Group.objects.get(id=request.urlparams[1])
		groups.save()
	#only allow superUsers to see all the groups
	if request.urlparams[0] == 'all':
		if not request.user.is_superuser:
	 	return HttpResponseRedirect('/')
		groups = m.Group.objects.all().order_by('zipcode')
	else:
		groups = m.Group.objects.all().order_by('zipcode')
	
	
	tvars = {
		'groups' : groups,
	}
	return templater.render_to_response(request, 'groups.html', tvars)

