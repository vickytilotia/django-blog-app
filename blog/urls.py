from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
    path('', views.home, name = 'homepage'),
    #to catch slug url of any blog post
    path('<slug:post>/', views.post_single, name = 'post_single'),
]
