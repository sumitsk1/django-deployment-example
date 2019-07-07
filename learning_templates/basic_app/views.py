from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context_dict = {'text':'hello this is text','number':1000}
    return render(request,"basic_app/index.html", context_dict)

def relative(request):
    return render(request,"basic_app/relative_url_templates.html")

def other(request):
    return render(request,"basic_app/other.html")
