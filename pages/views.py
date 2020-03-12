from django.template.response import TemplateResponse

# Create your views here.

def home(request):
    data = {
        'h1':"Craft",
        'subtitle':"This is a something",
        'title1':"One",
        'title2':"Twoo",
        'title3':"Three",
        'desc1': "One sed odio dui. Cras justo odio, dapibus ac facilisis in,egestas eget quam. Vestibulum id ligula porta felis euismodsemper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.",
        'desc2': "Two sed odio dui. Cras justo odio, dapibus ac facilisis in,egestas eget quam. Vestibulum id ligula porta felis euismodsemper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.",
        'desc3': "Three sed odio dui. Cras justo odio, dapibus ac facilisis in,egestas eget quam. Vestibulum id ligula porta felis euismodsemper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.",
        
    }
    return TemplateResponse(request,"home.html",data)

def about(request):
    return TemplateResponse(request,"about.html")

def index(request):
    return TemplateResponse(request, 'index.html')