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
]