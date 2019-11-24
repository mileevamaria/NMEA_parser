from django.shortcuts import render

def index(request):
    title = 'Данные GPS'
    context = {'title': title}
    return render(request, 'index.html', context)
