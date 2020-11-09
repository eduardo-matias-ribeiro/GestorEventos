from datetime import timezone

from django.db import models

# Create your models here.

class Curso(models.Model):
    nome_do_curso = models.CharField(max_length = 100)
    codigo_do_curso = models.IntegerField()

    def __str__(self):
        return self.nome_do_curso

class Funcionario(models.Model):
    nome_do_funcionario = models.CharField(max_length = 150)
    matricula = models.IntegerField()
    email_institucional = models.EmailField(max_length = 100)
    curso_vinculado =  models.ForeignKey(Curso, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_do_funcionario

class Palestrante(models.Model):
    nome_do_palestrante = models.CharField(max_length=150)
    dt_nascimento = models.DateField(auto_now = False , auto_now_add = False)
    cpf = models.CharField(max_length=14)
    email_pessoal = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome_do_palestrante


class Evento(models.Model):
    nome_do_evento = models.CharField(max_length = 200)
    data_inicio = models.DateTimeField(auto_now = False , auto_now_add = False, default="2020-11-09T13:20:30+03:00")
    data_final = models.DateTimeField(auto_now = False , auto_now_add = False, default="2020-11-09T13:20:30+03:00")
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    palestrante = models.ForeignKey(Palestrante, on_delete=models.RESTRICT)
    criador_do_evento = models.ForeignKey(Funcionario, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome_do_evento