from django.http.response import HttpResponse
from django.shortcuts import render


# Make django know in the settings.py regarding the template file
# TEMPLATES = [
    # {
    #     'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #     'DIRS': [BASE_DIR / 'templates'], <-----------

def homepage(request):
    return render(request, 'index/homepage.html')

def about(request):
    # request has the information about the request made by the user
    return render(request, 'about.html')