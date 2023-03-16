from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


# app_name = "clinc"
# urlpatterns = [
#     path('clinicas/', views.ClinicaViewSet.as_view()),
#     path('clinicas/<int:pk>/', views.ClinicaViewSet.as_view()),
#     path('medicos', views.MedicoViewSet.as_view()),
#     path('medicos/<int:pk>/', views.MedicoViewSet.as_view()),
#     path('pacientes', views.PacienteViewSet.as_view()),
#     path('pacientes/<int:pk>/', views.PacienteViewSet.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clinicas', views.ClinicaViewSet, basename='clinicas')
router.register(r'medicos', views.MedicoViewSet, basename='medicos')
router.register(r'pacientes', views.PacienteViewSet, basename='pacientes')
router.register(r'consultas', views.ConsultaViewSet, basename='consultas')
urlpatterns = router.urls
