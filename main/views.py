from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def blog(request):
    return render(request, 'main/blog.html')


def inspiration(request):
    return render(request, 'main/inspiration.html')


def about(request):
    return render(request, 'main/about.html')


# def connect(request):
#     return render(request, 'main/contacts_form.html')
