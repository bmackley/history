from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from homePage import models as m 
from . import templater

def process_request(request):
  new_sign = m.Sign()
  new_sign.id = 1
  new_sign.filepath = "/static/homePage/images/1-01.png"
  new_sign.name = "1"
  new_sign.mimeType = "1"
  new_sign.save()

  new_sign2 = m.Sign()
  new_sign2.id = 2
  new_sign2.filepath = "/static/homePage/images/10-01.png"
  new_sign2.name = "10"
  new_sign2.mimeType = "10"
  new_sign2.save()

  new_sign = m.Sign()
  new_sign.id = 3
  new_sign.filepath = "/static/homePage/images/2-01.png"
  new_sign.name = "2"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign2 = m.Sign()
  new_sign2.id = 4
  new_sign2.filepath = "/static/homePage/images/20-01.png"
  new_sign2.name = "20"
  new_sign2.mimeType = "20"
  new_sign2.save()
  
  new_sign = m.Sign()
  new_sign.id = 5
  new_sign.filepath = "/static/homePage/images/3-01.png"
  new_sign.name = "3"
  new_sign.mimeType = "3"
  new_sign.save()

  new_sign2 = m.Sign()
  new_sign2.id = 6
  new_sign2.filepath = "/static/homePage/images/30-01.png"
  new_sign2.name = "30"
  new_sign2.mimeType = "30"
  new_sign2.save()

  new_sign3 = m.Sign()
  new_sign3.id = 7
  new_sign3.filepath = "/static/homePage/images/4-01.png"
  new_sign3.name = "4"
  new_sign3.mimeType = "4"
  new_sign3.save()

  new_sign2 = m.Sign()
  new_sign2.id = 8
  new_sign2.filepath = "/static/homePage/images/40-01.png"
  new_sign2.name = "40"
  new_sign2.mimeType = "40"
  new_sign2.save()

  new_sign = m.Sign()
  new_sign.id = 9
  new_sign.filepath = "/static/homePage/images/5-01.png"
  new_sign.name = "5"
  new_sign.mimeType = "5"
  new_sign.save()

  new_sign2 = m.Sign()
  new_sign2.id = 10
  new_sign2.filepath = "/static/homePage/images/50-01.png"
  new_sign2.name = "50"
  new_sign2.mimeType = "50"
  new_sign2.save()
  new_sign = m.Sign()
  new_sign.id = 11
  new_sign.filepath = "/static/homePage/images/6-01.png"
  new_sign.name = "6"
  new_sign.mimeType = "6"
  new_sign.save()

  new_sign2 = m.Sign()
  new_sign2.id = 12
  new_sign2.filepath = "/static/homePage/images/60-01.png"
  new_sign2.name = "60"
  new_sign2.mimeType = "60"
  new_sign2.save()
  new_sign = m.Sign()
  new_sign.id = 13
  new_sign.filepath = "/static/homePage/images/7-01.png"
  new_sign.name = "7"
  new_sign.mimeType = "7"
  new_sign.save()

  new_sign2 = m.Sign()
  new_sign2.id = 14
  new_sign2.filepath = "/static/homePage/images/70-01.png"
  new_sign2.name = "70"
  new_sign2.mimeType = "70"
  new_sign2.save()
  tvars = {
  }
  return templater.render_to_response(request, 'login.html', tvars)
