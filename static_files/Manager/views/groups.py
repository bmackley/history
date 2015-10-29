from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m 
from . import templater

def process_request(request):
	'''Shows the List of Groups for SuperUsers, '''
	groups = m.Group.objects.get(id=request.urlparams[0])
	gid = request.urlparams[0]
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/Manager/login')
	if not request.user.is_superuser:
		if groups.administrator != request.user:
			return HttpResponseRedirect('/')
		else:
			members = m.Membership.objects.filter(group= groups)
	else:
		#only allow superUsers to see all the groups
		if request.urlparams[0] == 'all':
		 	groups = m.Group.objects.all().order_by('zipcode')
		else:
			members = m.Membership.objects.filter(group = groups)
			print(groups.groupName)
			for i in members:
				print(i.member.username)
				print(i.group.id)

	tvars = {
		'groups' : groups,
		'members' : members,
		'gid': gid,
	}
	return templater.render_to_response(request, 'groups.html', tvars)

