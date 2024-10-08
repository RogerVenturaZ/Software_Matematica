from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    # Página inicial
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    # URLs para Autor
    path('autores/', AutorListView.as_view(), name='autor_list'),
    path('autor/<int:pk>/', AutorDetailView.as_view(), name='autor_detail'),
    path('autor/<int:pk>/edit/', AutorUpdateView.as_view(), name='autor_update'),
    path('autor/<int:pk>/delete/', AutorDeleteView.as_view(), name='autor_delete'),

    # URLs para Tema
    path('temas/', TemaListView.as_view(), name='tema_list'),
    path('tema/<int:pk>/', TemaDetailView.as_view(), name='tema_detail'),
    path('tema/<int:pk>/edit/', TemaUpdateView.as_view(), name='tema_update'),
    path('tema/<int:pk>/delete/', TemaDeleteView.as_view(), name='tema_delete'),

    # URLs para História
    path('historias/', HistoriaListView.as_view(), name='historia_list'),
    path('historia/<int:pk>/', HistoriaDetailView.as_view(), name='historia_detail'),
    path('historia/<int:pk>/edit/', HistoriaUpdateView.as_view(), name='historia_update'),
    path('historia/<int:pk>/delete/', HistoriaDeleteView.as_view(), name='historia_delete'),

    # URLs para Comentário
    path('comentarios/', ComentarioListView.as_view(), name='comentario_list'),
    path('comentario/<int:pk>/', ComentarioDetailView.as_view(), name='comentario_detail'),
    path('comentario/<int:pk>/edit/', ComentarioUpdateView.as_view(), name='comentario_update'),
    path('comentario/<int:pk>/delete/', ComentarioDeleteView.as_view(), name='comentario_delete'),

    # URLs para Pergunta
    path('perguntas/', PerguntaListView.as_view(), name='pergunta_list'),
    path('perguntas/<int:pk>/edit/', PerguntaUpdateView.as_view(), name='pergunta_update'),
    path('perguntas/<int:pk>/delete/', PerguntaDeleteView.as_view(), name='pergunta_delete'),

    # URLs para Resposta
    path('respostas/', RespostaListView.as_view(), name='resposta_list'),
    path('respostas/<int:pk>/edit/', RespostaUpdateView.as_view(), name='resposta_update'),
    path('respostas/<int:pk>/delete/', RespostaDeleteView.as_view(), name='resposta_delete'),
]
