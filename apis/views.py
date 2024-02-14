from rest_framework import generics
from blog.models import Lugat
from .serializers import LugatSerializer

class LugatAPIView(generics.ListAPIView):
    queryset = Lugat.objects.all()
    serializer_class = LugatSerializer
    