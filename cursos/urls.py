from django.urls import path
from .views import AvaliacaoApiView, CursoApiView, CursosApiView, AvaliacoesApiView

urlpatterns = [
    path('cursos/', CursosApiView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoApiView.as_view(), name='curso'),
    path('avaliacoes/', AvaliacoesApiView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:pk>/', AvaliacaoApiView.as_view(), name='avaliacao'),
]
