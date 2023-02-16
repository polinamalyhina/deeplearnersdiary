from django.shortcuts import render
from .models import BlogPublications
from django.views.generic import DetailView

# Create your views here.


def blog(request):
    publications = BlogPublications.objects.all()
    return render(request, 'blogpart/blog.html', {'publications': publications})


class BlogDetailView(DetailView):
    model = BlogPublications
    template_name = "blogpart/detail_view.html"
    context_object_name = 'publication'

