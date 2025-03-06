from django.http import HttpResponse


# Simple view that returns a basic HTTP response
def home(request):
    return HttpResponse("Welcome to the home page!")


def new(request):
    return HttpResponse("Welcome to the new page!")


def next(request):
    return HttpResponse("Welcome to the next page to checkout now")

def legend(request):
    return HttpResponse("Welcome to the legend page to checkout now")

def micro(request):
    return HttpResponse("This is a micro response")