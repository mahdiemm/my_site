from django.db import models
from django.contrib.auth.models import User
from django_jalali.db.models import jDateField

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    slug = models.SlugField()
    body = models.TextField()
    date = jDateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='969.jpg',blank=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[0:80] + ' ...'
