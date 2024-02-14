from django.urls import path
from .views import LugatListView

    
urlpatterns = [
    path("", LugatListView.as_view(), name='lugat_list'),
]