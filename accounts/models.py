from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import escape, mark_safe
from django.core.validators import FileExtensionValidator

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, fullname, password=None):
        if not email:
            raise ValueError('user must have an email')
        else:
            email=self.normalize_email(email)
            user = self.model(email= email, fullname= fullname)
            user.set_password(password)
            user.save()


            return user
         
    def create_superuser(self, email, fullname, password=None):
        user = self.create_user(
            email=email,
            password=password,
            fullname=fullname,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()


        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=255, default=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    rules = models.BooleanField(default=False)
    phone_number = PhoneNumberField(blank=True, null=True)
    profile = models.ImageField(blank=True,default='default_profile.jpg')
    objects = MyUserManager()
    is_teacher = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname"]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.email
    
class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)
    

class Teacher(models.Model):
    TYPE = (
      ('TEACHER', 'teacher'),
      ('ORGANIZATIONS', 'organ'),
    )
    PAYMENT = (
      ('ZARIN', 'Zarin'),
    )
    userinfo = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=None)
    subject = models.ManyToManyField(Subject, related_name='subject')
    account = models.CharField(choices=TYPE,max_length=100)
    payment = models.CharField(choices=PAYMENT,max_length=100)
    identity = models.FileField(null=False,blank=False, upload_to='course_files/', validators=[FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])])
    documents = models.FileField(null=False,blank=False, upload_to='course_files/', validators=[FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])])
    body = models.TextField()

    def __str__(self):
        return self.userinfo.fullname




