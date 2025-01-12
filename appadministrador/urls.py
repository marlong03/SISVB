from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RolViewSet, UsuarioViewSet, TipoVotacionViewSet, PlanchaViewSet, VotoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'tipovotaciones', TipoVotacionViewSet)
router.register(r'planchas', PlanchaViewSet)
router.register(r'votos', VotoViewSet)
router.register(r'roles', RolViewSet)
urlpatterns = [
    path('', include(router.urls)),
]