from django.contrib import admin
from serie.models import Cargo, Cliente, Contato

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'nome', 
                    'fantasia', 
                    'cnpj', 
                    'logradouro', 
                    'numero', 
                    'bairro',
                    'cidade', 
                    'uf', 
                    'cep' )   
     
    fields = [('nome', 'fantasia'), 
              ('logradouro', 'complemento'),
              ('numero', 'bairro'), 
              ('cidade', 'uf'), 
              ('cep', 'cnpj', ),
              ('insc_estadual', 'insc_municipal'),
              ('serie', 'ativo'),
              ('observacao'),
              ('contato'),
              ]
          
    search_fields = ['id', 
                     'cidade', 
                     'nome', 
                     'fantasia', 
                     'cnpj']
    list_display_links = ('id', 
                          'nome')
    list_filter = ['id', 
                   'nome', 
                   'uf', 
                   'cidade', 
                   'bairro']
    list_per_page = 8

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'nome', 
                    'cpf',
                    'cargo', 
                    'email',
                    'fone', 
                    'celular', 
                    'celular_is_whatsapp',
                    'facebook', 
                    'twitter', 
                    'instagram', 
                    'ativo', 
                    'modificado')
    search_fields = ['id', 
                     'nome', 
                     'email']
    list_display_links = ('id', 
                          'nome')
    
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cargo', 'ativo', 'modificado')
    list_display_links = ('id', 'cargo')
    search_fields = ['id', 'cargo']
