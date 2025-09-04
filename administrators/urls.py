from django.urls import path
from . import views
app_name='administrators'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('assign/<int:report_id>/', views.assign_report, name='assign'),
]
