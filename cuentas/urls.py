from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, TipoCuentaViewSet, CuentaAhorroViewSet, TransaccionViewSet, realizar_deposito

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'tipos-cuenta', TipoCuentaViewSet)
router.register(r'cuentas-ahorro', CuentaAhorroViewSet)
router.register(r'transacciones', TransaccionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('depositar/', realizar_deposito, name='realizar_deposito'),
]