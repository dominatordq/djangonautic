from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')), # will look at all article urls 
    path('about/', views.about),
    path('', views.home)    # home page
]
