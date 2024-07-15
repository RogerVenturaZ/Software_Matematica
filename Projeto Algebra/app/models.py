from django.db import models

class Historia(models.Model):
    decada = models.CharField(max_length = 100)
    local = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 100)
    tema = models.CharField(max_length = 100)
    artigos = models.CharField(max_length = 100)
    
    class Meta:
        verbose_name_plural = "Historias"
    def __str__(self):
        return self.decada
 
 
class Autor(models.Model):
    nome = models.CharField(max_length = 100)
    endereco = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 100)
    cidade = models.CharField(max_length = 100) 
    
    class Meta:
        verbose_name_plural = "Autores"
    def __str__(self):
        return self.nome
       
class Tema(models.Model):
    nome = models.CharField(max_length = 100)
    data = models.CharField(max_length = 100)
    conteudo = models.CharField(max_length = 100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    
    
    
class Comentarios(models.Model):
    nome = models.CharField(max_length = 100)
    mensagem = models.CharField(max_length = 100)
    data = models.CharField(max_length = 100)
   
    
    
class Configuracao(models.Model):
    decada = models.CharField(max_length = 100)
    local = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 100)
    tema  = models.CharField(max_length = 100)
    artigos = models.CharField(max_length = 100)    
            
    
    
class Quiz(models.Model):
    nome = models.CharField(max_length = 100)
    posicao = models.CharField(max_length = 100)
    perguntas = models.CharField(max_length = 100)
    pontuacao = models.CharField(max_length = 100)    
    
    
    
    
    
# Create your models here.
