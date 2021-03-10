from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # allows Django to handle the serving of static files
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')), # will look at all article urls 
    path('about/', views.about),
    path('', views.home)    # home page
]

urlpatterns += staticfiles_urlpatterns()
