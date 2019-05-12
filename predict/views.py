from django.shortcuts import render
from django.views import View
from .forms import PhotoForm
from .models import Photo
import cv2
import tensorflow as tf
import keras
from keras.backend import tensorflow_backend as backend
import numpy as np
import glob
from django.conf import settings


loaded_model = keras.models.load_model(settings.MODEL_FILE_PATH)
graph = tf.get_default_graph()

class Top_page(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'predict/top_page.html')

top_page = Top_page.as_view()


def img_get(imgs):
    X = []
    for img_ in imgs:
        #path = img_.image.url
        path = img_
        img = cv2.imread(path)
        img = cv2.resize(img, dsize = (150,150))
        img = img.astype('float32')/255
        X.append(img)
        #X.append(path)

    X = np.array(X)
    return X

def pred(X):
    global graph
    with graph.as_default():
        result = []
        label = {0:'麻婆豆腐', 1:'ラーメン', 2:'かつ丼', 3:'カレー', 4:'から揚げ'}
        for x_ in X:
            x_ = x_.reshape(1, 150, 150, 3)
            pred = loaded_model.predict(x_)
            pred = pred.argmax()
            result.append(label[pred])
            #result.append(x_)
    return result


class Predict(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'predict/pred_1.html', {'form':PhotoForm(),})

    def post(self, request, *args, **kwargs):
        form = PhotoForm(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')

        photo = Photo()
        photo.image = form.cleaned_data['image']
        photo.save()

        imgs_1 = Photo.objects.all()
        imgs_2 = glob.glob('media/predict/*')
        X = img_get(imgs_2)
        result = pred(X)
        predict_results = []
        for i, j in zip(imgs_2, result):
            predict_results.append([i, j])

        return render(request, 'predict/pred_2.html', {'predict_results':predict_results},)

predict = Predict.as_view()
