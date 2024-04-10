from django.shortcuts import render



def index(request):
    return render(request, 'streaming/index.html')

def streaming(request):
    return render(request, 'streaming/streaming.html')

def sharing(request):
    return render(request, 'streaming/sharing.html')