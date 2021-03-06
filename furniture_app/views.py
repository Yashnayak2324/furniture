from furniture_app.models import Register
from django.shortcuts import render,redirect, resolve_url
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
            register = Register.objects.get(Email=vemail)
            if register.Password == vpassword:
                print(register.Password)
                print(vpassword)
                request.session['email'] = vemail
                request.session['fname']=register.Fname
                request.session['lname']=register.Lname
                request.session['image']=register.Image.url
                return render(request,'index.html')
            else:
                print("Password not Match.")
                msg="Password Not Matched !!"
                return render(request,'login.html',{'msg':msg})
        except:
            if vemail=="" or vpassword=="":
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
        del request.session['fname']
        del request.session['lname']
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
            vimage=request.FILES['image']
            print("1")
        except Exception as e:
            vimage="avtar.png"
            print(e)
        
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
                return render(request,'otp.html',{'gotp':otp,'email':vemail,'fname':vfname,'phoneno':vphoneno,'lname':vlname,'password':vpassword,'image':vimage})
    
    return render(request,'register.html')

def otp_var(request):
    votp=request.POST['otp']
    vgotp=request.POST['gotp']
    vemail=request.POST['email']
    vfname=request.POST['fname']
    vlname=request.POST['lname']
    vphoneno=request.POST.get('phone')
    vpassword=request.POST['pass']
    
    
    try:
        vimage=request.FILES['image']
        print(vimage)
    except:
        vimage="avtar.png"


    print(vimage)
    print("OTP : ",votp)
    print("GOTP : ",vgotp)
    print("Email : ",vemail)

    if votp==vgotp:
        register=Register.objects.create(Fname=vfname,Lname=vlname,Phoneno=vphoneno,Email=vemail,Password=vpassword,Image=vimage)
        msg="OTP verified successfully."
        return render(request,'login.html',{'msg':msg})
    else:
        msg="Please enter correct otp!"
        return render(request,'otp.html',{'msg':msg,'gotp':vgotp,'email':vemail,'fname':vfname,'lname':vlname,'password':vpassword,'image':vimage})

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

def change_password(request):
    register = Register.objects.get(Email=request.session['email'])

    if request.method=="POST":
        v_old_pass=request.POST['fopass']
        v_new_pass=request.POST['fnpass']
        v_new_confirm_pass=request.POST['fcnpass']

        password=register.Password
        print("---->",password)
        
        if v_old_pass!=register.Password:
            msg="Old Password Is Incorrect"
            return render(request,'change_password.html',{'msg':msg})

        elif v_old_pass==v_new_pass:
            msg="Please Enter Different Password"
            return render(request,'change_password.html',{'msg':msg})

        elif v_new_pass==v_new_confirm_pass:
            register.Password=v_new_pass
            register.save()
            return redirect('logout')
        else:
            msg="New Password And Confirm Password Is Not Matched"
            return render(request,'change_password.html',{'msg':msg})

        # if not match_pass:
        #     msg="Old Password Is Incorrect"
        #     return render(request,'change_password.html',{'msg':msg})
        # elif same_pass:
        #     msg="Please Enter Different Password"
        #     return render(request,'change_password.html',{'msg':msg})
        # elif v_new_pass==v_new_confirm_pass:
        #     user.Password = make_password(v_new_pass) 
        #     user.save()
        #     return redirect('logout')
        # else:
        #     msg="New Password And Confirm Password Is Not Matched"
        #     return render(request,'change_password.html',{'msg':msg})

    else:
        return render(request,'change_password.html')

def profile(request):
    register=Register.objects.get(Email=request.session['email'])
    if request.method=="POST":
        register.Fname=request.POST['fname']
        register.Lname=request.POST['lname']
        register.Phoneno=request.POST['phone']
        register.Add=request.POST['address']
        
        try:
            if request.FILES['pimage']:
                register.Image=request.FILES['pimage']
                register.save()

            del request.session['fname']
            del request.session['lname']
            del request.session['image']
            request.session['fname']=register.Fname
            request.session['lname']=register.Lname
            request.session['image']=register.Image.url
            register.save()
            msg="Profile Updated Successfully."
            print("1")
            return render(request,"profile.html",{'user':register,'msg':msg})
        except:
            register.save()
            del request.session['fname']
            del request.session['lname']
            request.session['fname']=register.Fname
            request.session['lname']=register.Lname
            print("2")
            msg="Profile Updated Successfully."
            return render(request,"profile.html",{'user':register,'msg':msg})
    else:
        return render(request,"profile.html",{'user':register})

    
def pvc_furniture(request):
    return render(request,"pvc_furniture.html",)

def kitchen_cabiinet(request):
    img=Kitchen_Images.objects.all()
    return render(request,"pvc furniture/kitchen_cabiinet.html",{'img':img})

def wardrobe(request):
    img=Wardrobe_Image.objects.all()
    return render(request,"pvc furniture/wardrobe.html",{'img':img})

def tvcabinet(request):
    img=Tvcabinet_Image.objects.all()
    return render(request,'pvc furniture/tvcabinet.html',{'img':img})

def pvc_door(request):
    img=Pvcdoor_Image.objects.all()
    return render(request,'pvc furniture/pvc_door.html',{'img':img})

def ceiling(request):
    img=Designerceiling_Image.objects.all()
    return render(request,'pvc furniture/ceiling.html',{'img':img})

def wall_panelling(request):
    img=Wallpanelling_Image.objects.all()
    return render(request,'pvc furniture/wall_panelling.html',{'img':img})

def upvc_window(request):
    img=Upvcwindow_Image.objects.all()
    return render(request,'pvc furniture/upvc_window.html',{'img':img})

def partition(request):
    img=Pvcparition_Image.objects.all()
    return render(request,'pvc furniture/partition.html',{'img':img})

def contact(request):
    if request.method=="POST":
        vname=request.POST['name']
        vemail=request.POST['email']
        vsubject=request.POST['subject']
        vmessage=request.POST['message']

        Contact.objects.create(Name=vname,Email=vemail,Subject=vsubject,Message=vmessage)
        msg="Contact Saved Successfully"
        return render(request,'contact.html',{'msg':msg})
    else:
        return render(request,'contact.html')








