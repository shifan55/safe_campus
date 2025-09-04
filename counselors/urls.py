from django.urls import path
from . import views
app_name='counselors'
urlpatterns = [ path('', views.dashboard, name='dashboard') ]
