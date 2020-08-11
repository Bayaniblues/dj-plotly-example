from django.urls import path

from . import views
# import dash apps here
from plotlyapps.dash_apps import SimpleExample


urlpatterns = [
    path('', views.index, name='index'),
]

