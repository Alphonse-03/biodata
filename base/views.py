from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base/home2.html')
def about(request):
    return render(request,'base/about.html')
def skill(request):
    return render(request,'base/skills.html')
def dream(request):
    return render(request,'base/dream.html')