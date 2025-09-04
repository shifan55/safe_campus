from django.urls import path
from . import views
app_name='students'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('report/', views.report_form, name='report_form'),
    path('thanks/', views.report_thanks, name='report_thanks'),
]
