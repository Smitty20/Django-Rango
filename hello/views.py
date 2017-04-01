from django.http import HttpResponse
import time

def index(request):
    return HttpResponse("Hello, human! Current date is: " + time.strftime("%c"))