from django.conf.urls import url
from Signapp import views

urlpatterns = [
    url(r'^$', views.StartPageView.as_view()),
    url(r'^index/$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
]
