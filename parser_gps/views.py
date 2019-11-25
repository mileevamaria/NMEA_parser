from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from parser_gps.func import *
import os
import re

def index(request):
    title = 'Данные GPS'

    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        file = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(file)
        filename = re.sub('/media/', '', url)
        context = {'title': title, 'url': url, 'filename': filename}
        return render(request, 'index.html', context)

    context = {'title': title}
    return render(request, 'index.html', context)

def file_content(request, filename):
    title = 'Посмотреть данные'
    filepath = os.path.join('media', filename)
    data = nmea_get(filepath)
    print(data)

    if request.method == "GET":
        height = request.GET.get('height_query')
        diff_height = request.GET.get('diff_height')
        speed = request.GET.get('speed_query')
        diff_speed = request.GET.get('diff_speed')

        filtered_data = nmea_filter(data, height, diff_height, speed, diff_speed)
        context = {'title': title, 'data': filtered_data, "filename": filename}
        return render(request, 'file_content.html', context)

    context = {'title': title, 'data': data, "filename": filename}
    return render(request, 'file_content.html', context)
