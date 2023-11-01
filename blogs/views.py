from django.shortcuts import render, HttpResponse
from . import models
from django.views.generic import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class BlogsView(FormView):
    template_name ='blogs_list.html'



def blog_list(request):
    blogs = models.Blogs.objects.all().order_by('-time')
    num_blogs = blogs.count()
    paginator = Paginator(blogs , 6)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(1)
    args = {'blogs':blogs, 'page':page, 'num_blogs':num_blogs} 
    return render(request, 'blogs/blogs_list.html', args)


def blog_detail(request, slug):
    blog = models.Blogs.objects.get(slug=slug)
    return render(request , 'blogs/blog_detail.html', {'blog':blog})
