from furniture_app.models import Register
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from random import *
from django.conf import settings
from .utils import *
from django.contrib import messages
import random




# Create your views here.

def base(request):
    return render(request,'index.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def products(request):
    return render(request,'products.html')

def register(request):
    if request.method=="POST":
        vfname=request.POST['fname']
        vlname=request.POST['lname']
        vemail=request.POST['email']
        vpassword=request.POST['pass']
        vcpassword=request.POST['cpassword']

        try:
            reg = Register.objects.get(Email=vemail)
            if reg:
                msg="This Email Id Already Registerd With Us"
                return render(request,'register.html',{'msg':msg})
        except:
            if vfname=="" or vlname=="" or vemail== "" or vpassword=="" or vcpassword=="":
                msg="Plz Enter All Fileds"
                return render(request,'register.html',{'msg':msg})
            elif vpassword!=vcpassword:
                msg="Plz Enter Same Password"
                return render(request,'register.html',{'msg':msg})
            else:
                # register=Register.objects.create(Fname=vfname,Lname=vlname,Email=vemail,Password=vpassword)
                # msg="You Are Register Successfully"
                # return render(request,'login.html',{'msg':msg})

                otp = randint(100000,999999)
                email_Subject = 'OTP  For Signup Verfication'
                sendmail(email_Subject,'otpVerification_emailTemplate',vemail,{'name':'Dear User','otp':otp})
                return render(request,'otp.html',{'gotp':otp,'email':vemail,'fname':vfname,'lname':vlname,'password':vpassword})
    return render(request,'register.html')

def otp_var(request):
    votp=request.POST['otp']
    vgotp=request.POST['gotp']
    vemail=request.POST['email']
    vfname=request.POST['fname']
    vlname=request.POST['lname']
    vpassword=request.POST['pass']

    print("OTP : ",votp)
    print("GOTP : ",vgotp)
    print("Email : ",vemail)

    if votp==vgotp:
        register=Register.objects.create(Fname=vfname,Lname=vlname,Email=vemail,Password=vpassword)
        msg="OTP verified successfully."
        return render(request,'login.html',{'msg':msg})
    else:
        msg="Please enter correct otp!"
        return render(request,'otp.html',{'msg':msg,'gotp':vgotp,'email':vemail,'fname':vfname,'lname':vlname,'password':vpassword})




def single(request):
    return render(request,'single.html')





