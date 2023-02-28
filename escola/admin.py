from django.contrib import admin
from escola.models import Aluno, Professor

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )

class Professores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'curso')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'curso', )
    
admin.site.register(Aluno, Alunos,)
admin.site.register(Professor, Professores,)