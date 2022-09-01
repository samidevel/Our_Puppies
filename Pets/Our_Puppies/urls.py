from django.urls import path
from .import views


urlpatterns = [
	path('', views.userpublication, name='publication')
]
