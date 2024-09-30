from django.urls import path

from .views import ManApiView

urlpatterns = [
    path('manlist/', ManApiView.as_view())
]