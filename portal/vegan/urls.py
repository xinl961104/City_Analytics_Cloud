from django.conf.urls import url
from .views import get_data, ChartData
from . import views


urlpatterns = [
    url(r'^education/$', views.home, name='home'),
    url(r'^$', views.firstpage, name='firstpage'),
    url(r'^income/$', views.income, name='income'),
    url(r'^donation/$', views.donation, name='donation'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
]
