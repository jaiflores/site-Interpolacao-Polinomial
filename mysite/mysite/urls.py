from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]


# Configure Admin Titles
admin.site.site_header = "MySite Adminitration page"
admin.site.site_title = "MySite"
admin.site.index_title = "MySite"

