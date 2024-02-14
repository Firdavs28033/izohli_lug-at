from django.urls import path 
from .views import LugatAPIView

urlpatterns = [ 
    path("", LugatAPIView.as_view(), name = "lugat_api"),
]