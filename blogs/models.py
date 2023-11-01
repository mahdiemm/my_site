from django.db import models
from django.contrib.auth.models import User
from django_jalali.db.models import jDateField
from django.utils.translation import gettext as _

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    slug = models.SlugField()
    body = models.TextField()
    date = jDateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='969.jpg',blank=True, max_length=100)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[0:80] + ' ...'



# class Comment(models.Model):
#     blog =models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name="comments")
#     name = models.CharField(_("نام"), max_length=50)
#     body = models.TextField()
#     created = jDateTimeField(auto_now_add=True) 
#     updated = jDateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('-created',)

#     def __str__(self):
#         return f'comment by {self.name} on {self.blog}' 
