from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clinicas', views.ClinicaViewSet, basename='clinicas')
router.register(r'medicos', views.MedicoViewSet, basename='medicos')
router.register(r'pacientes', views.PacienteViewSet, basename='pacientes')
router.register(r'consultas', views.ConsultaViewSet, basename='consultas')
urlpatterns = router.urls
