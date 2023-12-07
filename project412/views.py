from django.shortcuts import render, HttpResponse,redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
import cv2
import tensorflow as tf
import numpy as np
from joblib import load
from django.shortcuts import render
from .forms import ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from tensorflow import keras
from joblib import load
import os
from .forms import ContactForm
from django.contrib import messages
from project412.models import Contact
from datetime import datetime
from django.db import migrations
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from project412.models import UserProfile
from django.contrib.auth.models import User
from Project import settings
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})

def predict_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['image']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = os.path.join(settings.MEDIA_ROOT, filename)

            # Load the model
            Cnn_model = load(r'G:\412-project-main\Project\savedModels\Cnn_model.joblib')

            # Preprocess the image
            img = keras.preprocessing.image.load_img(file_path, target_size=(150, 150))
            img_array = keras.preprocessing.image.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0)  # Create a batch

            # Make predictions
            predictions = Cnn_model.predict(img_array)
            class_index = tf.argmax(predictions[0]).numpy()
            class_labels = ['Cyst', 'Normal', 'Stone', 'Tumor']
            predicted_class = class_labels[class_index]

            # Delete the uploaded file
            os.remove(file_path)

            return render(request, 'predict_result.html', {'predicted_class': predicted_class})
    else:
        form = ImageUploadForm()

    return render(request, 'predict_image.html', {'form': form})


def devs(request):
    return render(request,'devs.html')
"""
def registration_signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('signup')  # Redirect to a success page
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {'form': form})
"""
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def signup(request):
    if request.method=="GET":
        return render(request,'signup.html')
    
    elif request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        mobile=request.POST.get('mobile')
        profile_picture = request.FILES.get('profile_picture')

        myuser= UserProfile(
            fname=fname,
            lname=lname,
            password=password,
            email=email,
            dob=dob,
            gender=gender,
            mobile=mobile,
            profile_picture=profile_picture


        )
        print("email:",email)
        if not (fname and lname and email and password and dob and gender and mobile and profile_picture):
            return render(request, 'signup.html', {'Prompt': 'Please fill in all the required fields'})

        if UserProfile.objects.filter(email=email).exists():
            return render(request,'signup.html',{'Prompt':'Email Already Exist'})
        
        else:
            myuser = User.objects.create_user(username=email,first_name=fname,last_name=lname,password=password,email=email)

            myuser.save()
            ins=UserProfile(fname=fname,lname=lname,email=email,password=password,
                                         dob=dob,gender=gender,mobile=mobile, profile_picture=profile_picture)
            ins.save()
            user=authenticate(email=email,password=password)

            if user is not None:
                login(request,user)
                return redirect("index")
            
            else:
                return render(request,'signup.html')


def log_in(request):
    if request.method == "GET":
        return render(request, "login.html", {"name": "UserProfile"})
    
    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        print("Email:", email)
        print("Password:", password)
        user = authenticate(username=email, password=password)

        print(user)

        if user is not None:
            login(request,user)
            if user.is_staff==True:
                print("username:",email)
                print("password:",password)
                return redirect(reverse('admin:index'))
                #return render(request, "/loc_admin")
            elif user.is_staff==False:
                return render(request, "user_profile.html")
        else:
            return render(request, "login.html", {"name": "UserProfile","prompt":"Sorry UserName or Password is invalid !"})
    


    
        

    

def user_profile(request):
    return render(request,'user_profile.html')