from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),   # <-- ADD THIS
    path('api/', include('students.urls')),        # (optional)
]
