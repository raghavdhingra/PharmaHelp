#Imports statement
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from main.serializer import *
from rest_framework import status
import json
import requests
from rest_framework.views import APIView
from django.contrib.auth.models import User,Group
from .models import *
from django.core.mail import send_mail
# Create your views here.

#APIs
class LabList(APIView):
    def get(self,request):
        member = Labs.objects.all()
        serializer = LabsSerializer(member, many=True)
        return JsonResponse(serializer.data,safe=False)

    def post(self):
        pass


def home(request):
    context = {
        "title": "Home",
    }
    return render(request,'home.html',context)

def lab(request):
    lab = []
    if request.method == 'POST':
        sort_option = request.POST.get('sort_option')
        if sort_option == 'Rating':
            data = requests.get('http://hackinit.herokuapp.com/labapi')
            resp = json.loads(data.text)
            lab = sorted(resp, key = lambda i: i['rating']) 
        elif sort_option == 'Price':
            data = requests.get('http://hackinit.herokuapp.com/labapi')
            resp = json.loads(data.text)
            lab = sorted(resp, key = lambda i: i['price']) 
        elif sort_option == 'Certified':
            for x in Labs.objects.all():
                if x.certified == True:
                    lab.append(x)
        elif sort_option == 'Availability':
            for x in Labs.objects.all():
                if x.availability == True:
                    lab.append(x)

        context = {
            "title": "Find Labs",
            "lab":lab,
        }
        return render(request,'lab.html',context)
    context = {
        "title": "Find Labs",
        "lab":Labs.objects.all(),
    }
    return render(request,'lab.html',context)

def pharmacy(request):
    context = {
        "title": "Find Pharmacies",
    }
    return render(request,'pharmacy.html',context)

def recommend(request):
    context = {
        "title": "Your Recommendation",
    }
    return render(request,'recommend.html',context)

def sendMail(request):
    if_online = True
    if request.method == 'POST':
        name = str(request.POST.get('firstname')) + " " + str(request.POST.get('lastname'))
        service = request.POST.get('service')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        msg = request.POST.get('message')

        mail_message = "{}\n{}\n{}\n{}\n{}\n{}\n".format(name,service,phone,date,time,msg)
    if if_online == True:
        send_mail(
            'Consultation query',
            mail_message,
            'contact@helloworldofficial.in',
            ['fakeassprofilee@gmail.com','fakeassprofilee@yahoo.com'],
            fail_silently=False,
        )
    else:
        send_mail(
            'Consultation query',
            mail_message,
            'contact@helloworldofficial.in',
            ['fakeassprofilee@gmail.com','fakeassprofilee@yahoo.com'],
            fail_silently=False,
        )
    return redirect('/')


