from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Autor, Tema, Historia, Comentario, Pergunta, Resposta
from .forms import AutorForm, TemaForm, HistoriaForm, ComentarioForm, PerguntaForm, RespostaForm
from django.views import View 

# Views para Autor
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class AutorListView(ListView):
    model = Autor
    template_name = 'autor_list.html'
    context_object_name = 'autores'

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autor_detail.html'
    context_object_name = 'autor'

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor_update.html'
    success_url = reverse_lazy('autor_list')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autor_delete.html'
    success_url = reverse_lazy('autor_list')

# Views para Tema
class TemaListView(ListView):
    model = Tema
    template_name = 'tema_list.html'
    context_object_name = 'temas'

class TemaDetailView(DetailView):
    model = Tema
    template_name = 'tema_detail.html'
    context_object_name = 'tema'

class TemaUpdateView(UpdateView):
    model = Tema
    form_class = TemaForm
    template_name = 'tema_update.html'
    success_url = reverse_lazy('tema_list')

class TemaDeleteView(DeleteView):
    model = Tema
    template_name = 'tema_delete.html'
    success_url = reverse_lazy('tema_list')

# Views para História
class HistoriaListView(ListView):
    model = Historia
    template_name = 'historia_list.html'
    context_object_name = 'historias'

class HistoriaDetailView(DetailView):
    model = Historia
    template_name = 'historia_detail.html'
    context_object_name = 'historia'

class HistoriaUpdateView(UpdateView):
    model = Historia
    form_class = HistoriaForm
    template_name = 'historia_update.html'
    success_url = reverse_lazy('historia_list')

class HistoriaDeleteView(DeleteView):
    model = Historia
    template_name = 'historia_delete.html'
    success_url = reverse_lazy('historia_list')

# Views para Comentário
class ComentarioListView(ListView):
    model = Comentario
    template_name = 'comentario_list.html'
    context_object_name = 'comentarios'

class ComentarioDetailView(DetailView):
    model = Comentario
    template_name = 'comentario_detail.html'
    context_object_name = 'comentario'

class ComentarioUpdateView(UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario_update.html'
    success_url = reverse_lazy('comentario_list')

class ComentarioDeleteView(DeleteView):
    model = Comentario
    template_name = 'comentario_delete.html'
    success_url = reverse_lazy('comentario_list')

# Views para Pergunta
class PerguntaListView(ListView):
    model = Pergunta
    template_name = 'pergunta_list.html'
    context_object_name = 'perguntas'

class PerguntaUpdateView(UpdateView):
    model = Pergunta
    form_class = PerguntaForm
    template_name = 'pergunta_update.html'
    success_url = reverse_lazy('pergunta_list')

class PerguntaDeleteView(DeleteView):
    model = Pergunta
    template_name = 'pergunta_delete.html'
    success_url = reverse_lazy('pergunta_list')

class RespostaListView(ListView):
    model = Resposta
    template_name = 'resposta_list.html'
    context_object_name = 'respostas'

class RespostaUpdateView(UpdateView):
    model = Resposta
    form_class = RespostaForm
    template_name = 'resposta_update.html'

    def get_success_url(self):
        return reverse_lazy('resposta_list')

class RespostaDeleteView(DeleteView):
    model = Resposta
    template_name = 'resposta_delete.html'
    success_url = reverse_lazy('resposta_list')




