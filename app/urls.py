from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addblog/', views.addblog, name='addblog'),
    path('deleteblog/<int:id>', views.deleteblog, name='deleteblog'),
]