# myapp/forms.py
from django import forms
from .models import Autor, Tema, Historia, Pergunta, Resposta, Comentario

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'endereco', 'email', 'telefone', 'cidade']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Seu email'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Seu telefone'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Sua cidade'}),
        }
        labels = {
            'nome': 'Nome do Autor',
            'endereco': 'Endereço',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'cidade': 'Cidade',
        }

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['nome', 'conteudo', 'autor']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Conteúdo do tema'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome do Tema',
            'conteudo': 'Conteúdo',
            'autor': 'Autor',
        }

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = ['decada', 'local', 'autor', 'tema', 'artigos']
        widgets = {
            'artigos': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Artigos relacionados'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'tema': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'decada': 'Década',
            'local': 'Local',
            'autor': 'Autor',
            'tema': 'Tema',
            'artigos': 'Artigos',
        }

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ['texto', 'pontuacao']  # Removido o campo 'quiz'
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Texto da pergunta'}),
        }
        labels = {
            'texto': 'Texto da Pergunta',
            'pontuacao': 'Pontuação',
        }

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['texto', 'correta']
        widgets = {
            'texto': forms.TextInput(attrs={'placeholder': 'Digite o texto da resposta...'}),
            'correta': forms.CheckboxInput(),
        }
        labels = {
            'texto': 'Resposta',
            'correta': 'Correta',
        }
        help_texts = {
            'texto': 'Insira o texto da resposta.',
            'correta': 'Marque se esta resposta é a correta.',
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'mensagem']  # Atualizado para refletir o modelo Comentario
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Digite seu comentário'}),
        }
        labels = {
            'nome': 'Nome',
            'mensagem': 'Comentário',
        }
