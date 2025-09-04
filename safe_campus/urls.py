from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('students/', include('students.urls')),
    path('counselors/', include('counselors.urls')),
    path('administrators/', include('administrators.urls')),
    path('', home, name='home'),
]
