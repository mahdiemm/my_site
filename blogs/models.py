from django.db import models
# from django.contrib.auth.models import User
from django_jalali.db.models import jDateField, jDateTimeField
from django.utils.translation import gettext as _
from accounts.models import CustomUser

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(CustomUser,default=None,on_delete=models.CASCADE)
    slug = models.SlugField()
    body = models.TextField()
    date = jDateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='969.jpg',blank=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[0:80] + ' ...'



class Comment(models.Model):
    blog =models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name="comments")
    name = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="user_comments")
    body = models.TextField()
    created = jDateTimeField(auto_now_add=True) 
    updated = jDateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'comment by {self.name.fullname} on {self.blog}' 
    
    
class AnswerComment(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name="answer_comments")
    name = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="user_answer_comments")
    answer = models.TextField() 
    created = jDateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-date',) 
    def __str__(self):
        return f'comment by {self.name.fullname} on {self.comment}'
