from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to our amazing application!")

def dashboard(request):
    return HttpResponse("This is your personalized dashboard with all the latest updates.")

def about(request):
    return HttpResponse("Learn more about our innovative platform and services.")    