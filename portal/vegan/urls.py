from django.conf.urls import url
from .views import get_data, ChartData
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
]
