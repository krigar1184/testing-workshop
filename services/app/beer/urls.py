from django.conf.urls import url
from beer import views


app_name = 'beer'
urlpatterns = [
    url(r'beer/(?P<pk>\d+)$', views.BeerUpdateDeleteView.as_view(), name='detail'),
    url(r'beer/$', views.BeerListView.as_view(), name='list'),
    url(r'beer/create$', views.BeerCreateView.as_view(), name='create'),
    url(r'beer/edit$', views.BeerUpdateDeleteView.as_view(), name='edit'),
]
