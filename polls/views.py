from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.http import HttpResponse
from .predict import ans
# q = Question.__str__
# from django.template import loader
# from .forms import *
from django.conf import settings
import cv2 as cv


def upload(request):
    print(request.method)
    img = ""
    num = -1
    if request.method == "POST":
        uploaded =  request.FILES["photo"]
        # path += uploaded.name
        # print(path)
        fs  = FileSystemStorage()
        name = fs.save(uploaded.name,uploaded)
        img = fs.url(name)
        # print(img)
        num = ans('static/images/'+uploaded.name)
        # print(x)
        # form = ImageForm(request.POST,request.FILES)
        # # print(request.FILES["document"].name)
        # if form.is_valid():
        #     form.save()
        #     return redirect('success')
    # else :
    #     form = ImageForm()
    # print (settings.STATIC_ROOT + '/templates/polls/index.html')
    return render(request, 'polls/index.html',{'direct' : img , 'Predict' :num })