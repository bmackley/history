from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from homePage import models as m 
from . import templater

def process_request(request):
  print(request.user)
  form = LoginForm()
  
  if request.method == 'POST':

    form = LoginForm(request.POST)
    if form.is_valid():
      userN = form.cleaned_data['username'].lower()
      user = authenticate(username = userN, password = form.cleaned_data['password'])
      if user is not None:
        login(request, user)
        redirect = request.META.get('HTTP_REFERER')
        #returns them to the page they were on
        return HttpResponse('<script>window.location.href="'+ redirect +'"</script>')    
  tvars = {
  'form' : form,
  }

  return templater.render_to_response(request, 'login.html', tvars)

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

  def clean(self):
    uName = self.cleaned_data['username'].lower()
    print(uName)
    user = authenticate(username = uName, password = self.cleaned_data['password'])
    if user == None:
      raise forms.ValidationError("Incorrect password or Username") 
    return self.cleaned_data