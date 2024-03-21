from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContantAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'description', 'show', 'picture'] #Campos que vão aparecer
    ordering = ['-id'] #Ordem decrecente de exibição
    list_filter = ['created_date'] #Filtro que vai ficar ao lado, criados na ultima semana, no ultimo mês, etc
    search_fields = ['id', 'first_name', 'last_name'] # Campos que eu posso buscar
    list_per_page = 10 #Quantidade de usuários por página
    list_max_show_all = 1000 #Só vai mostrar todos se tiver no máximo 1000 usuário
    list_editable = ['first_name', 'last_name'] # Campos que podem ser editados mais facilmente
    list_display_links = ['id', 'phone'] # Link para acessar a página de edição

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
