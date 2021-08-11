from django.db import models
from string import ascii_lowercase # para fazer loop alfabeto
from taggit.managers import TaggableManager
from django.utils.html import format_html

# python manage.py migrate --run-syncbd

class Fonte(models.Model):
    nome = models.CharField(max_length=30)
    ano = models.IntegerField(default=2020, blank=True)

    class Meta:
        ordering = ['nome', 'ano']
    
    def save(self, *args, **kwargs):
        if not Fonte.objects.filter(nome= self.nome, ano= self.ano ):# Fonte.objects.filter():
            super().save(*args, **kwargs)
        else:
            pass

    def __str__(self):
        return "%s - %s" % (self.nome.upper(), self.ano)

class TipoAssunto(models.Model):
    nome = models.CharField(max_length=10, editable = True)
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return "%s" % (self.nome)

class Assunto(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoAssunto, on_delete=models.CASCADE) 

    class Meta:
        ordering = ['nome', 'tipo']
        managed = True
    
    def save(self, *args, **kwargs):
        if not Assunto.objects.filter(nome= self.nome, tipo= self.tipo ):# Fonte.objects.filter():
            super().save(*args, **kwargs)
        else:
            pass
    
    def __str__(self):
        return "%s" % (self.nome)

class Questao(models.Model):
    choices_tipo = [
        (0,  'Objetiva'),
      (1, 'Discusiva'),
      (2, 'Somatória')
    ]
      
    fonte = models.ForeignKey(Fonte, on_delete=models.CASCADE, default=0)
    tipo = models.PositiveSmallIntegerField(
      choices=choices_tipo,
      default=0,
   ) 
    choices_disciplina = [
        (0,  'Física')
    ]
    disciplina = models.PositiveSmallIntegerField(
      default=0,
      choices = choices_disciplina
   )  
    assunto_princ = models.ForeignKey(Assunto, on_delete=models.CASCADE)#models.ManyToManyField(Assunto)
    assuntos_sec = TaggableManager(blank=True)

    editado = models.BooleanField('A questão já foi corrigida.', default=False)
    # editado.short_description = 
    # editado.allow_tags = True

    choices_dificuldade = [
        (0,  '1'),
        (1, '2'),
        (2, '3'),
        (3, '4'),
        (4, '5'),
        (5, '6'),
        (6, '7'),
        (7, '8'),
        (8, '9'),
        (9, '10'),
    ]

    dificuldade = models.PositiveSmallIntegerField(default=5,
    choices = choices_dificuldade)
    enunciado = models.TextField(blank=True)
    figura = models.ImageField(upload_to='figures/', blank=True)
    pergunta = models.TextField(blank=True)
    dados = models.CharField(max_length=200, blank=True)
    resolucao = models.TextField(blank=True)

    nr_utilizacoes = models.IntegerField(default=0)

    data_inc = models.DateTimeField('data_inc', auto_now_add=True)
    data_modificacao = models.DateTimeField('data_mod', auto_now=True)

    def __str__(self):
        resposta = "(%s) %s\n\n %s\n\n %s \n\n " % (self.fonte, self.enunciado, self.pergunta, self.dados)
        
        alternativas = Alternativas.objects.filter(questao=self.id)
        if alternativas:
            alfabeto = "abcdefghijlmnopqrstuvxz"
            i = 0
            inicio = ''
            fim = ''
            for item in alternativas:
                if item.gabarito == True:
                    inicio = r'***'
                #     fim = r'}'
                
                resposta += inicio+'('+alfabeto[i]+') '+item.texto +fim+'\n\n\n'
                i += 1
                inicio = ''
                # fim = '' 
        # print(alternativas)
        return  resposta


    def figura_tag(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.figura.url))
        
    figura_tag.short_description = ''
    figura_tag.allow_tags = True
    
    texto_t = models.TextField(blank=True)
    questao_t = models.TextField(blank=True)
    resolucao_t =models.TextField(blank=True)
    texto_fig = models.ImageField(upload_to='figures/tratamento', blank=True)
    questao_fig = models.ImageField(upload_to='figures/tratamento', blank=True)
    resolucao_fig = models.ImageField(upload_to='figures/tratamento', blank=True)

    def texto_fig_tag(self):
        return format_html('<img href="{0}" src="{0}" />'.format(self.texto_fig.url))
    texto_fig.short_description = ''
    texto_fig.allow_tags = True

    def questao_fig_tag(self):
        return format_html('<img href="{0}" src="{0}" />'.format(self.questao_fig.url))
    questao_fig.short_description = ''
    questao_fig.allow_tags = True

    def resolucao_fig_tag(self):
        return format_html('<img href="{0}" src="{0}" />'.format(self.resolucao_fig.url))
    resolucao_fig.short_description = ''
    resolucao_fig.allow_tags = True

    class Meta:
        ordering = ['data_inc']
        verbose_name = 'Questão'
        verbose_name_plural = "Questões"
    
    def save(self, *args, **kwargs):        
        super().save(*args, **kwargs)
        
class Alternativas(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE) 
    texto = models.TextField()
    gabarito = models.BooleanField('Resposta certa', default=False)
    choices_ordem = [
        (0,  '1'),
        (1, '2'),
        (2, '3'),
        (3, '4'),
        (4, '5'),
        (5, '6'),
        (6, '7'),
        (7, '8'),
        (8, '9'),
        (9, '10'),
    ]

    ordem = models.PositiveSmallIntegerField(default=5,
    choices = choices_ordem, unique=True)

    def __str__(self):
        return "%s" % (self.texto)

    class Meta:
        verbose_name_plural = "Alternativas"

# class Exame(models.Model):
#     choices_disciplina = [
#         (0,  'Física'),
#         # (1, 'Médio')
#     ]
#     disciplina = models.PositiveSmallIntegerField(default=1,
#     choices = choices_disciplina)
#     choices_ensino = [
#         (0,  'Fundamental'),
#         (1, 'Médio')
#     ]
#     ensino = models.PositiveSmallIntegerField(default=1,
#     choices = choices_ensino)  #SESI
#     questoes = models.ManyToManyField(Questao, blank=True)
#     assuntos = models.ManyToManyField(Assunto, blank= True)
#     data_inc = models.DateTimeField('data_inc', auto_now_add=True)
#     data_modificacao = models.DateTimeField('data_mod', auto_now=True)
#     choices_escola = [
#         (0,  'SESI'),
#         (1, 'CEJA M'),
#         (2, 'CEJA BR'),
#         (3, 'CEJARJ'),
#         (4, 'SANTA AMÉLIA')
#     ]
#     turma = models.CharField(max_length=200, blank=True)#SESI
#     escola = models.PositiveSmallIntegerField(default=5,
#     choices = choices_escola)
#     nr_questoes = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(1)]
#     )
#     bimestre = models.PositiveSmallIntegerField(default=1,
#     choices = [(1, '1°'), (2, '2°'), (3, '3°'), (4, '4°')])#SESI
#     prof = models.CharField(max_length=200, blank=True, default= "Leonardo Marques", editable=False)
#     qr_code = models.ImageField(upload_to='figures/qr', blank=True)

#     class Meta:
#         managed = True 