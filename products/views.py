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
        title_query = self.request.query_params.get('title')

        if title_query:
            # Case-insensitive title filtering
            queryset = queryset.filter(
                Q(title__icontains=title_query)
            )

        return queryset

