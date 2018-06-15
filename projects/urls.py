from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^projects/', views.project_list, name='project_list'),
    
]