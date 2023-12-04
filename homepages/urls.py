from django.urls import path
from .views import indexPageView, aboutPageView, instrumentPageView, trumpet_detail_view

urlpatterns = [
    path('', indexPageView, name='index'),
    path('homepages/about/', aboutPageView, name ='about'),
    path('inventory/instrument/', instrumentPageView, name='instrument'),
    path('trumpet/<str:instrument_name>/<int:instrument_id>/', trumpet_detail_view, name='trumpet_view'),
]

