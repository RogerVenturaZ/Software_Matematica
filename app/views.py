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

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autordelete.html'
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

class TemaCreateView(CreateView):
    model = Tema
    form_class = TemaForm
    template_name = 'tema_form.html'
    success_url = reverse_lazy('tema_list')

class TemaUpdateView(UpdateView):
    model = Tema
    form_class = TemaForm
    template_name = 'tema_form.html'
    success_url = reverse_lazy('tema_list')

class TemaDeleteView(DeleteView):
    model = Tema
    template_name = 'temadelete.html'
    success_url = reverse_lazy('tema_list')

# Views para Historia
class HistoriaListView(ListView):
    model = Historia
    template_name = 'historia_list.html'
    context_object_name = 'historias'

class HistoriaDetailView(DetailView):
    model = Historia
    template_name = 'historia_detail.html'
    context_object_name = 'historia'

class HistoriaCreateView(CreateView):
    model = Historia
    form_class = HistoriaForm
    template_name = 'historia_form.html'
    success_url = reverse_lazy('historia_list')

class HistoriaUpdateView(UpdateView):
    model = Historia
    form_class = HistoriaForm
    template_name = 'historia_form.html'
    success_url = reverse_lazy('historia_list')

class HistoriaDeleteView(DeleteView):
    model = Historia
    template_name = 'historiadelete.html'
    success_url = reverse_lazy('historia_list')

# Views para Comentario
class ComentarioListView(ListView):
    model = Comentario
    template_name = 'comentario_list.html'
    context_object_name = 'comentarios'

class ComentarioDetailView(DetailView):
    model = Comentario
    template_name = 'comentario_detail.html'
    context_object_name = 'comentario'

class ComentarioCreateView(CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario_form.html'
    success_url = reverse_lazy('comentario_list')

class ComentarioUpdateView(UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario_form.html'
    success_url = reverse_lazy('comentario_list')

class ComentarioDeleteView(DeleteView):
    model = Comentario
    template_name = 'comentario_confirm_delete.html'
    success_url = reverse_lazy('comentario_list')

# Views para Pergunta
class PerguntaListView(ListView):
    model = Pergunta
    template_name = 'pergunta_list.html'
    context_object_name = 'perguntas'

class PerguntaCreateView(CreateView):
    model = Pergunta
    form_class = PerguntaForm
    template_name = 'pergunta_form.html'
    success_url = reverse_lazy('pergunta_list')

class PerguntaUpdateView(UpdateView):
    model = Pergunta
    form_class = PerguntaForm
    template_name = 'pergunta_form.html'
    success_url = reverse_lazy('pergunta_list')

class PerguntaDeleteView(DeleteView):
    model = Pergunta
    template_name = 'pergunta_confirm_delete.html'
    success_url = reverse_lazy('pergunta_list')

# Views para Resposta
class RespostaListView(ListView):
    model = Resposta
    template_name = 'resposta_list.html'
    context_object_name = 'respostas'

    def get_queryset(self):
        pergunta_id = self.kwargs.get('pergunta_id')
        return Resposta.objects.filter(pergunta_id=pergunta_id)

class RespostaCreateView(CreateView):
    model = Resposta
    form_class = RespostaForm
    template_name = 'resposta_form.html'
    success_url = reverse_lazy('resposta_list')

class RespostaUpdateView(UpdateView):
    model = Resposta
    form_class = RespostaForm
    template_name = 'resposta_form.html'
    success_url = reverse_lazy('resposta_list')

class RespostaDeleteView(DeleteView):
    model = Resposta
    template_name = 'resposta_confirm_delete.html'
    success_url = reverse_lazy('resposta_list')

# Funções adicionais para Pergunta e Resposta
def listar_perguntas(request, pergunta_id):
    # A variável quiz_id não existe mais, pois a classe Quiz foi removida.
    perguntas = get_object_or_404(Pergunta, id=pergunta_id)
    return render(request, 'perguntas/listar_perguntas.html', {'pergunta': perguntas})

def criar_pergunta(request):
    if request.method == "POST":
        form = PerguntaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pergunta_list')  # Redirecionar após sucesso
    else:
        form = PerguntaForm()
    return render(request, 'perguntas/criar_pergunta.html', {'form': form})

def editar_pergunta(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, id=pergunta_id)
    if request.method == "POST":
        form = PerguntaForm(request.POST, instance=pergunta)
        if form.is_valid():
            form.save()
            return redirect('pergunta_list')
    else:
        form = PerguntaForm(instance=pergunta)
    return render(request, 'perguntas/editar_pergunta.html', {'form': form, 'pergunta': pergunta})

def deletar_pergunta(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, id=pergunta_id)
    pergunta.delete()
    return redirect('pergunta_list')

def listar_respostas(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, id=pergunta_id)
    respostas = Resposta.objects.filter(pergunta=pergunta)
    return render(request, 'respostas/listar_respostas.html', {'pergunta': pergunta, 'respostas': respostas})

def criar_resposta(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, id=pergunta_id)
    if request.method == "POST":
        form = RespostaForm(request.POST)
        if form.is_valid():
            resposta = form.save(commit=False)
            resposta.pergunta = pergunta
            resposta.save()
            return redirect('listar_respostas', pergunta_id=pergunta.id)
    else:
        form = RespostaForm()
    return render(request, 'respostas/criar_resposta.html', {'form': form, 'pergunta': pergunta})

def editar_resposta(request, resposta_id):
    resposta = get_object_or_404(Resposta, id=resposta_id)
    if request.method == "POST":
        form = RespostaForm(request.POST, instance=resposta)
        if form.is_valid():
            form.save()
            return redirect('listar_respostas', pergunta_id=resposta.pergunta.id)
    else:
        form = RespostaForm(instance=resposta)
    return render(request, 'respostas/editar_resposta.html', {'form': form, 'resposta': resposta})

def deletar_resposta(request, resposta_id):
    resposta = get_object_or_404(Resposta, id=resposta_id)
    pergunta_id = resposta.pergunta.id
    resposta.delete()
    return redirect('listar_respostas', pergunta_id=pergunta_id)
