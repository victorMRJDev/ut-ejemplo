from rest_framework.routers import DefaultRouter
from producto.api.views import ProductoViewSet

router = DefaultRouter()
# router.register('productos', 'productos', ProductoViewSet)
router.register('productos', ProductoViewSet, basename='productos')
urlpatterns = router.urls