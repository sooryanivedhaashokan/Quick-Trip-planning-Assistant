from django.conf.urls import url
from kunju import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view()),
]
