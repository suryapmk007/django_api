from rest_framework import viewsets
from .models import product
from .serializers import productSerializer


class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer
