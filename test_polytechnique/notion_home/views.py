from django.shortcuts import render

def home(request):
    return render(request, 'notion_home/home.html')