from django.contrib import admin
from .models import Produto


@admin.register(Produto)  # decoret serve para registrar
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')
