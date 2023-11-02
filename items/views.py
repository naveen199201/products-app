# views.py
from rest_framework import viewsets
from .models import Product
from django.db.models import Q
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        title = self.request.query_params.get('title',None)

        if title:
            # Case-insensitive title filtering
            queryset = queryset.filter(
                Q(title__icontains=title)
            )

        return queryset

    