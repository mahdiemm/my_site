from django.db import models
from django.contrib.auth.models import User
from django_jalali.db.models import jDateField
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')
    

class Questions(models.Model):
    title = models.ForeignKey("Courses", on_delete=models.CASCADE)
    question= models.TextField()
    answer= models.TextField()


class Courses(models.Model):
    STATUS = (
        ("draft",'Draft'),
        ("published",'Published')
    )
    TYPE = (
        ("course",'Course'),
        ("special",'Special'),
        ("Doing",'doing')
    )
    SUBJECT = (
        ("medical",'Medical'),
        ("nursing",'Nursing'),
        ("my_uni",'My_uni'),
        ("coming_soon",'Coming_soon')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    subject = models.CharField(max_length=20,choices=SUBJECT,default='coming_soon')
    date = jDateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    upadated = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=10,choices=TYPE,default='course')
    image = models.ImageField(default='',blank=True)
    price = models.IntegerField(blank=True, default=0) 
    slug = models.SlugField(max_length=250)
    status = models.CharField(max_length=10,choices=STATUS,default='draft')
    objects = models.Manager()
    published = PublishedManager()
    header = models.ImageField(default='',blank=True)
    file = models.FileField(default='',blank=True)
    prerequisite = models.TextField(blank=True)
    content = models.TextField(blank=True)
    about = models.TextField()
    recommender = models.ManyToManyField(User, related_name="recommender_course", blank=True, default=None)
    like = models.ManyToManyField(User, related_name="like_post", blank=True)
    tag = TaggableManager()
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)


    

class Lessons(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    course = models.ForeignKey("Courses", on_delete=models.CASCADE)
    video = models.URLField(max_length=200)
    summary = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    
















