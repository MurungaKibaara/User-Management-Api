from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^api/', include('djoser.urls')),
    # re_path(r'^api/', include('djoser.urls.jwt')),
    re_path(r'^api/', include('spauser.urls')),
]
