from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'items', ProductViewSet)

urlpatterns = [
    # Other URL patterns, if any
]

urlpatterns += router.urls
