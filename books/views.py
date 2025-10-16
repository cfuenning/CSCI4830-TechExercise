from django.shortcuts import render

#The render function generates HTTP response
#These functions handle HTTP requests and return HTTP response
def index(request): 
    return render(request, 'index_hello.html') 

def about(request):
    return render(request, 'about_hello.html')

'''
SUPER SIMPLE CODE TO TEST IF SERVER WORKED:

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world!!!")
'''