from django.urls import path

from . import views


urlpatterns = [ 
    path('', views.index, name='Index'),
    path('result', views.result, name='result'),
    # path('final', views.final, name='final')
]