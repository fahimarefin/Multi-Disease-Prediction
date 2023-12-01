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



def index(request):
    return render(request,'index.html')

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


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form data saved:", form.cleaned_data)  # Add this line for debugging
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('index')
        else:
            print("Form errors:", form.errors)  # Add this line for debugging
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

