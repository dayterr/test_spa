from django.urls import path

from . import views

from .forms import SearchForm

urlpatterns = [
    path('', views.TableView.as_view(), name='index'),
]
