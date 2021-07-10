from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.base,name='base'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('products/',views.products,name='products'),
    path('register/',views.register,name='register'),
    path('single/',views.single,name='single'),
    path('otp_var/',views.otp_var,name='otp_var'),
    path('logout/',views.logout,name='logout'),
    path("showemail/",views.showemail,name="showemail"),
    path("sendotp/",views.sendotp,name="sendotp"),
    path("otp_forget_pw",views.otp_forget_pw,name="otp_forget_pw"),
    path("forget_password/",views.forget_password,name="forget_password"),
    path('change_password/',views.change_password,name='change_password'),
    path('profile/',views.profile,name='profile'),
    path('pvc_furniture/',views.pvc_furniture,name='pvc_furniture'),
    path('contact/',views.contact,name='contact'),
    path('kitchen_cabiinet/',views.kitchen_cabiinet,name='kitchen_cabiinet'),
    path('wardrobe/',views.wardrobe,name='wardrobe'),
    path('tvcabinet/',views.tvcabinet,name='tvcabinet'),
    path('pvc_door/',views.pvc_door,name='pvc_door'),
    path('ceiling/',views.ceiling,name='ceiling'),
    path('wall_panelling/',views.wall_panelling,name='wall_panelling'),
    path('upvc_window/',views.upvc_window,name='upvc_window'),
    path('partition/',views.partition,name='partition'),
]
