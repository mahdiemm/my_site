from django.shortcuts import render, redirect
from . import models
from django.views.generic import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, AnswerCommentForm
from django.http import HttpResponseRedirect
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
    comments = blog.comments.all()
    num_comments = comments.count()    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            if request.user.is_authenticated:
                new_comment.name = request.user
            else:
                return redirect('accounts:login')
            new_comment.blog = blog
            new_comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()
        answer_comment_form = AnswerCommentForm()
    args ={
        'blog':blog,
        'form':comment_form,
        'comments':comments,
        'num_comments':num_comments,
        'answer_form': answer_comment_form
    }
    return render(request , 'blogs/blog_detail.html',args)



