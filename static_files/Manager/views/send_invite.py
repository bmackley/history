from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from Manager import HTMLEmailInvite as EmailInv
from . import templater
import decimal, datetime
from django.utils.timezone import utc
from django.contrib.auth import authenticate, login
from django import forms
from django.core.mail import EmailMultiAlternatives

def process_request(request):
	gid = request.urlparams[0]	
	form = addUser(initial={
		'userInvite':""
		})
	print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
	print(gid)
	print('bbbbbbbbbbbbbbbbbbbbbbbbbb')
	if request.method == 'POST':
		form = addUser(request.POST)
		if form.is_valid():
			toEmail = form.cleaned_data['userInvite']
			message = "Your friends have invitedYour friends have invited you to CompFITition"  " \r\nFollow this link to join:\r\n\r\n\r\nAfter you have created an account, click this link to join the group"
			htmlMessage ="<h1>Your friends have invited you to join CompFITition.com!</h1><br><h2>click here to sign up:<h2><br><a href='www.compfitition.com/member/create_user'>Sign up</a></br> Once you have signed up, please join the group <i>Beta Group</i>"
			'''
			"Once you have signed up, click here to join your friend's group <br><a href='www.compfitition.com/member/join/"+ gid+ "'>Join</a>" 
			'''
			msg = EmailMultiAlternatives('Compete with your friends', EmailInv.inviteEmail, 'ben@compFITition.com', [toEmail])
			msg.attach_alternative(EmailInv.inviteEmail, "text/html")
			msg.send()
			print(message)
			return HttpResponseRedirect('/Manager/send_invite/${gid}')

	tvars={
	'form': form,
		'gid': gid,
	}
	
	return templater.render_to_response(request, 'send_invite.html', tvars)
	
class addUser(forms.Form):
	userInvite = forms.CharField(required=True, label="Enter E-mail", widget=forms.TextInput(attrs={'class':'form-control'}))
		
