from django.urls import path
from .views import AvaliacaoApiView, CursoApiView

urlpatterns = [
    path('cursos/', CursoApiView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacaoApiView.as_view(), name='avaliacoes'),
]
