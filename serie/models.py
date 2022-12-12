from django.db import models

SIM_NAO_CHOICE = [
    (None, ''),
    (True, 'Sim'),
    (False, 'Não'),
]

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True

class Contato(Base):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, blank=True)
    cargo = models.ForeignKey('Cargo', verbose_name='Cargo', on_delete=models.PROTECT)
    email = models.EmailField('Email', max_length=200, blank=True, null=True)
    fone = models.CharField('Fone', max_length=9, blank=True, null=True)    
    celular = models.CharField('Celular', max_length=9, blank=True, null=True)   
    celular_is_whatsapp = models.CharField('É WhatsApp', max_length=1, blank=True, null=True)     
    facebook = models.CharField('Facebook', max_length=100, blank=True, null=True)
    twitter = models.CharField('Twitter', max_length=100, blank=True)
    instagram = models.CharField('Instagram', max_length=100, blank=True, null=True)
    obs = models.CharField('Observação', max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        
    def __str__(self):
        return self.nome    

class Cliente(Base):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    fantasia = models.CharField(max_length=100, blank=True, null=True, verbose_name='Fantasia')
    cnpj = models.CharField(max_length=14, unique=True, blank=True, null=False, verbose_name='CNPJ')
    insc_estadual = models.CharField('IE', max_length=14, blank=True)
    insc_municipal = models.CharField('Insc.Munic.', max_length=14, blank=True)
    serie = models.CharField(max_length=20, blank=True, null=True, verbose_name='Número Série')
    serie_dt = models.DateTimeField(blank=True, null=True, verbose_name='Dt.Serie')
    bairro = models.CharField(max_length=50, blank=True, null=True, verbose_name='Bairro')
    cep = models.CharField(max_length=8, blank=True, null=True, verbose_name='CEP')
    complemento = models.CharField(max_length=35, blank=True, null=True, verbose_name='Complemento')
    logradouro = models.CharField(max_length=150, blank=True, null=True, verbose_name='Logradouro')
    numero = models.IntegerField(verbose_name='Número')
    uf = models.CharField(max_length=2, blank=True, null=True, verbose_name='UF')
    observacao = models.CharField(max_length=100, blank=True, null=True, verbose_name='Observação')
    contato = models.ManyToManyField(Contato, blank=True, null=True, verbose_name='Contato')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nome']
        db_table = 'cliente'
  
class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        
    def __str__(self):
        return self.cargo