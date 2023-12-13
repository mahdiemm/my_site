from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from . import models
from .models import Courses
from django.views.generic import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, AnswerCommentForm
from django.http import HttpResponseRedirect
# Create your views here.

class BlogsView(FormView):
    template_name ='course_list.html'



def courses_list(request):
    courses = models.Courses.objects.all().order_by('-date')
    num_courses = courses.count()
    paginator = Paginator(courses , 6)
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(1)
    args = {'courses':courses,
            'num_courses': num_courses,
            'page':page
        }
    return render(request, 'courses/course_list.html', args)


def course_detail(request, slug):
    course = models.Courses.objects.get(slug=slug)
    questions = models.Questions.objects.all()
    videos = models.Lessons.objects.all()
    num_video = 0
    comments = course.comments.all()
    num_comments = comments.count()    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            if request.user.is_authenticated:
                new_comment.name = request.user
            else:
                return redirect('accounts:login')
            new_comment.course = course
            new_comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()
        answer_comment_form = AnswerCommentForm()
    
    for video in videos:
        if video.course.id == course.id:
            num_video = num_video+1

    
    content ={
        'course':course,
        'questions':questions,
        'videos':videos,
        'num_video':num_video,
        'form':comment_form,
        'comments':comments,
        'num_comments':num_comments,
        'answer_form': answer_comment_form
    }
    return render(request , 'courses/course_detail.html', content)
