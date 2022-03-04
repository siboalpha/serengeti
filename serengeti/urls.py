from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
]

admin.site.site_header = "SERENGETI Admin"
admin.site.site_title = "SERENGETI Admin Portal"
admin.site.index_title = "Welcome to SERENGETI Portal"