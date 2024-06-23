from django.urls import path
from . import views

urlpatterns = [
    path("", views.mountains, name='mountains'),
    path('forecast/<str:name>', views.forecast, name='forecast'),
]
