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

def products(request):
    return render(request,'products.html')


def login(request):
    if request.method == "POST":
        vemail = request.POST['femail']
        vpassword = request.POST['fpass']
        try:
            user = Register.objects.get(Email=vemail)

            if user.Password == vpassword:
                print(user.Password)
                print(vpassword)
                request.session['email'] = vemail
                return render(request,'index.html')
            else:
                print("Password not Match.")
                msg="Password Not Matched !!"
                return render(request,'login.html',{'msg':msg})
        except:
            if vemail=="" or vpass=="":
                msg="Please enter both fileds!"
                return render(request,'login.html',{'msg':msg})
            else:
                msg="Email id is not registered !"
                return render(request,'login.html',{'msg':msg})
            
    else:
        return render(request,'login.html')

def logout(request):
    try:
        del request.session['email']
        return render(request,'login.html')
    except:
        return render(request,'login.html')

def register(request):
    if request.method=="POST":
        vfname=request.POST['fname']
        vlname=request.POST['lname']
        vemail=request.POST['email']
        vphoneno=request.POST['phone']
        vpassword=request.POST['pass']
        vcpassword=request.POST['cpassword']

        try:
            reg = Register.objects.get(Email=vemail)
            if reg:
                msg="This Email Id Already Registerd With Us"
                return render(request,'register.html',{'msg':msg})
        except:
            if vfname=="" or vlname=="" or vemail== "" or vphoneno=="" or vpassword=="" or vcpassword=="":
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
                return render(request,'otp.html',{'gotp':otp,'email':vemail,'fname':vfname,'phoneno':vpohneno,'lname':vlname,'password':vpassword})
    
    return render(request,'register.html')

def otp_var(request):
    votp=request.POST['otp']
    vgotp=request.POST['gotp']
    vemail=request.POST['email']
    vfname=request.POST['fname']
    vlname=request.POST['lname']
    vphoneno=request.POST['phone']
    vpassword=request.POST['pass']

    print("OTP : ",votp)
    print("GOTP : ",vgotp)
    print("Email : ",vemail)

    if votp==vgotp:
        register=Register.objects.create(Fname=vfname,Lname=vlname,Phoneno=vphoneno,Email=vemail,Password=vpassword)
        msg="OTP verified successfully."
        return render(request,'login.html',{'msg':msg})
    else:
        msg="Please enter correct otp!"
        return render(request,'otp.html',{'msg':msg,'gotp':vgotp,'email':vemail,'fname':vfname,'lname':vlname,'password':vpassword})




def single(request):
    return render(request,'single.html')

def showemail(request):
    return render(request,'showemail.html')

def sendotp(request):
    vemail=request.POST['email']
    register=Register.objects.filter(Email=vemail)
    if register:
        otp = randint(100000,999999)
        email_Subject = "OTP For Forget Passwrod"
        sendmail(email_Subject,'otpVerification_emailTemplate',vemail,{'name':'Dear User','otp':otp})

        return render(request,"otp_forget_pw.html",{'gotp':otp,'email':vemail})
    else:
        msg="Enter valid Email Id" 
        return render(request,"showemail.html",{'msg':msg})

def otp_forget_pw(request):

    vemail=request.POST['email']
    vgotp=request.POST['gotp']
    votp=request.POST['otp']
    
    if vgotp==votp:
        return render(request,"forget_password.html",{'email':vemail})
    else:
        msg="Incorect OTP !"
        return render(request,"otp_forget_pw.html",{'msg':msg,'email':vemail,'gotp':vgotp})

def forget_password(request):

    vemail=request.POST['email']
    vpassword=request.POST['pass']
    vcpassword=request.POST['cpass']
    register=Register.objects.get(Email=vemail)
    
    if vpassword==vcpassword:
        register.Password=vpassword
        register.save()
        
        msg="Password changed successfully."
        return render(request,"login.html",{'msg':msg})
    else:
        msg="Password does not match!"
        return render(request,"forget_password.html",{'msg':msg,'email':vemail,'role':vrole})








