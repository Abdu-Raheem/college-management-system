from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('principal/', include('principalapp.urls')),
    path('hod/', include('hodapp.urls')),
    path('tutor/', include('tutorapp.urls')),
    path('student/', include('studentapp.urls')),
]
