from django.urls import path 
from . import views


app_name = "accounts"
urlpatterns = [
    path('register/', views.register_user  , name="register"),
    path('login',views.login_view, name='login'),
    path('pages/terms', views.rules , name="rules"),
    path('become-instructor/', views.teacher_request , name="teacher_request"),
]