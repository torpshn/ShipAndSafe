from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name = 'search'),
    path(r'^show/$', views.show, name = 'show')
]