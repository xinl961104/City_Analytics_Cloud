from django.conf.urls import url
from .views import get_data, ChartData
from . import views


urlpatterns = [
    url(r'^topic1/$', views.home, name='home'),
    url(r'^income/$', views.income, name='income'),
    url(r'^lifeExpectancy/$', views.lifeExpectancy, name='lifeExpectancy'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
]
