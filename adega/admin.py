from django.contrib import admin
from .models import Adega

class AdegaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'qtd_vinhos', 'created', 'updated']
    list_filter = ['qtd_vinhos']
    search_fields = ['nome']

admin.site.register(Adega, AdegaAdmin)


