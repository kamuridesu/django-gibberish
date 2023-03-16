from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = "clinc"
urlpatterns = [
    path('clinicas/', views.ListaDeClinicas.as_view()),
    path('clinicas/<int:pk>/', views.DetalhesClinica.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
