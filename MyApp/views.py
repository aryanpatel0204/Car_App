from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.conf import settings
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    try:
        MyUser.objects.get(email=request.session['email'])
        return redirect(logout)
    except:
        return render(request,'index.html')
    
def login(request):
    if request.method=="POST":
        try:
            MyUser.objects.get(
                email=request.POST['email'],
                password=request.POST['password']
            )
            return render(request,'index.html')
        except Exception as e:
            print("Error: ",e)
            msg="Email Or Password Are Incorrect!!"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request,'login.html')
    except:
        return render(request,'login.html')
    
def signup(request):
    if request.method=='POST':
        try:
            MyUser.objects.get(
                email=request.POST['email'],
				password=request.POST['password']
            )
            msg='Email Already Registered.'
            return render(request,'signUp.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                MyUser.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						password=request.POST['password'],
						cpassword=request.POST['cpassword'],
						address=request.POST['address'],
						genderType=request.POST['genderType'],
                        city=request.POST['city'],
                        state=request.POST['state'],
                        zipCode=request.POST['zipCode']
					)
                msg="User Sign Up Successfully!!Go To Your Registered Email Id For OTP."
                user=MyUser.objects.get(email=request.POST['email'])
                return render(request,'login.html',{'email':user.email,'msg':msg})
            else:
                msg = 'Passwords do not match.'
                return render(request,'signUp.html',{'msg': msg})
    else:
        return render(request,'signUp.html')
def allcars(request):
    return render(request,'more_cars.html')