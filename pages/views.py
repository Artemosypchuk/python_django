from django.template.response import TemplateResponse

# Create your views here.

def home(request):
    return TemplateResponse(request,"home.html")

def about(request):
    return TemplateResponse(request,"about.html")