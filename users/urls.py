from django.conf.urls import url
# from django.core import views as core_views

from . import views

urlpatterns = [
url(r'^signup/$', views.signup, name='signup'),
]