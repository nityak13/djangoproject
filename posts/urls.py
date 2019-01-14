from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #^ start with $ end with nothing
    url(r'/details(?P<id>\d+)', views.details, name='details')
]
