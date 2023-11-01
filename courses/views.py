from django.shortcuts import render, HttpResponse, get_object_or_404
from . import models
from .models import Courses
from django.views.generic import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    for video in videos:
        if video.course.id == course.id:
            num_video = num_video+1
    content ={
        'course':course,
        'questions':questions,
        'videos':videos,
        'num_video':num_video
    }
    return render(request , 'courses/course_detail.html', content)
