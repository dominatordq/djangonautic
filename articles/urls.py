from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.article_list),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail),   # [\w-]+ -- \w = any word or number, - = hyphens can be used, + = any length
    #path('<slug:slug>', views.article_detail)
]
