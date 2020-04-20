from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.http import HttpResponse
from .predict import ans
# q = Question.__str__
# from django.template import loader
# from .forms import *
from django.conf import settings
# import cv2 as cv


def upload(request):
    print(request.method)
    img = "/images/image-icon.png"
    num = -1
    if request.method == "POST":
        try:
            uploaded = request.FILES["photo"]
        except KeyError:
            uploaded = "nothing"
        # uploaded =  request.FILES["photo"]
        if uploaded == "nothing" :
            return render(request, 'polls/index.html',{'direct' : img })
        else :
            fs  = FileSystemStorage()
            name = fs.save(uploaded.name,uploaded)
            img = fs.url(name)
            # print(img)
            num ,percent= ans('static/images/'+uploaded.name)
            if percent < 0.25 :
                num = "NAN"
                percent = 1
            return render(request, 'polls/index.html',{'direct' : img , 'Predict' :num ,'Percent':percent*100.0 })

        # print(uploaded.name)
        # path += uploaded.name
        # print(path)
       
    return render(request, 'polls/index.html',{'direct' : img })
