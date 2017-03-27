from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index),
url(r'^users$', views.create_user),
url(r'^travels$', views.travels),
url(r'^logout$', views.logout),
url(r'^session$', views.login_user),
url(r'^add$', views.add_trip),
url(r'^create_trip$', views.create_trip),
url(r'^user_trips$', views.user_trips),
url(r'^destinations/(?P<id>\d+)$', views.destinations),

]
