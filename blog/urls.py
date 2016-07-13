from django.conf.urls include,url
from . import views

ulrpatterns=[url(r'^$',views.post_list),]
