from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from parser_gps.func import nmea
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
        print(filename, url)
        context = {'title': title, 'url': url, 'filename': filename}
        return render(request, 'index.html', context)

    context = {'title': title}
    return render(request, 'index.html', context)

def file_content(request, filename):
    title = 'Посмотреть данные'
    filepath = os.path.join('media', filename)
    data = nmea(filepath)

    context = {'title': title, 'data': data}
    return render(request, 'file_content.html', context)
