from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Questions)
admin.site.register(models.Courses)
admin.site.register(models.Lessons)
admin.site.register(models.CourseComment)
admin.site.register(models.AnswerCourseComment)



