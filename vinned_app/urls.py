from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='index'),
    # path('results/', views.vin_info),
    path('results', views.vin_info, name = 'results'),
]