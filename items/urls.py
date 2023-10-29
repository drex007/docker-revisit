
from django.urls import path
from .views import ItemsApiView
urlpatterns = [
    path('all', ItemsApiView.as_view())
]
