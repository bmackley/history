from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime
from django.contrib.auth import authenticate, login

def process_request(request):	
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
		
	group = m.Group.objects.get(id=request.urlparams[0])
	user = request.user
	newMember = m.Membership()
	newMember.group = group
	newMember.member = user
	print(newMember.group)
	print(newMember.member)
	newMember.save()



	tvars={
	
	}
	
	return templater.render_to_response(request, 'join.html', tvars)
	
