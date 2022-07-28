from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.get_route, name="default"),
]
