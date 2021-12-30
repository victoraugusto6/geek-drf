from django.urls import path
from .views import AvaliacaoApiView, CursoApiView, CursosApiView, AvaliacoesApiView

urlpatterns = [
    path('cursos/', CursosApiView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoApiView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesApiView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoApiView.as_view(), name='curso_avaliacao'),

    path('avaliacoes/', AvaliacoesApiView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoApiView.as_view(), name='avaliacao'),
]
