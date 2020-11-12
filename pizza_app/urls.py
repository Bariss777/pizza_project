#from django.conf.urls import url
from django.urls import path

from pizza_app.views import create, view, close, stats, menu, history

urlpatterns = [
    path('create/', create, name='create'),
    # view/<int:pizza_order_id>
    path('view/(?P<pizza_order_id>[0-9]+)/', view, name='view'),
    path('close/(?P<pizza_order_id>[0-9]+)/', close, name='close'),
    path('menu/', menu, name='menu'),
    path('history/', history, name='history'),
    path('stats/', stats, name='stats'),
]
