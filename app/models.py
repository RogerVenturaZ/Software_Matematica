from django.db import models
from django.utils import timezone

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Autores"
    
    def __str__(self):
        return self.nome

class Tema(models.Model):
    nome = models.CharField(max_length=100)
    conteudo = models.TextField()  # Use TextField para textos maiores
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='temas')
    
    class Meta:
        verbose_name_plural = "Temas"
    
    def __str__(self):
        return self.nome

class Historia(models.Model):
    decada = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='historias')
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='historias')
    artigos = models.TextField()  # Use TextField para textos maiores
    
    class Meta:
        verbose_name_plural = "Historias"
    
    def __str__(self):
        return f'{self.decada} - {self.tema}'

class Comentario(models.Model):
    nome = models.CharField(max_length=100)
    mensagem = models.TextField()  # Use TextField para mensagens mais longas
    data = models.DateTimeField(auto_now_add=True)  # Use DateTimeField para a data do comentário
    
    class Meta:
        verbose_name_plural = "Comentarios"
    
    def __str__(self):
        return f'{self.nome} - {self.data}'


class Pergunta(models.Model):
    texto = models.TextField()
    pontuacao = models.IntegerField()

    class Meta:
        verbose_name_plural = "Perguntas"

    def __str__(self):
        return self.texto

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas')
    texto = models.CharField(max_length=255, help_text='Texto da resposta')
    class Meta:
        verbose_name_plural = "Respostas"

    def __str__(self):
        return self.texto
