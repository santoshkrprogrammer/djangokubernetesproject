from django.http import HttpResponse


# Simple view that returns a basic HTTP response
def home(request):
    return HttpResponse("Welcome to the home page!")