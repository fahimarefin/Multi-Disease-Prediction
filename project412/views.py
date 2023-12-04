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

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Updated to use the URL name
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

def registration_signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('signup')  # Redirect to a success page
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {'form': form})




def log_in(request):
    if request.method == "GET":
        return render(request, "login.html", {"name": "UserProfile"})

    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        print("Email:", email)
        print("Password:", password)

        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_active:

            print("Authentication successful")
            login(request, user)

            if user.is_staff:
                # Redirect to admin dashboard or whatever is appropriate for staff members
                return redirect(reverse('admin:index'))
            else:
                # Redirect to the user profile page for regular users
                print("Redirecting to user_profile")
                return redirect(reverse('user_profile'))
        else:
            print("Authentication failed")
            return render(request, "login.html", {"name": "UserProfile", "prompt": "Sorry UserName or Password is invalid !"})


def user_profile(request):
    return render(request,'user_profile.html')
