from django.db import models

# Create your models here.
class Paciente(models.Model):
  cpf = models.CharField(max_length=11, unique=True)
  nome_completo = models.CharField(max_length=200)
  nome_social = models.CharField(max_length=200)
  data_nasc = models.DateField(auto_now=False, auto_now_add=False)
  SEXOS = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro')
  )
  sexo = models.CharField(max_length=2, choices=SEXOS)
  cor = models.CharField(max_length=10)
  num_casa = models.CharField(max_length=6)
  rua = models.CharField(max_length=50)
  bairro = models.CharField(max_length=50)
  complemento = models.CharField(max_length=100)
  municipio = models.CharField(max_length=50)
  sp = models.CharField(max_length=2)
  cep = models.CharField(max_length=8)
  religiao = models.CharField(max_length=50)
  nome_mae = models.CharField(max_length=200, blank=True)
  nome_pai = models.CharField(max_length=200, blank=True)
  telefone = models.CharField(max_length=14)
  class Meta:
    ordering = ['nome_completo']
  def __str__(self):
      return self.nome_completo

