from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def signup(request):
    return render(request,'signup.html')
def login(request):
    return render(request,'login.html')
def expert(request):
    return render(request,'expert.html')