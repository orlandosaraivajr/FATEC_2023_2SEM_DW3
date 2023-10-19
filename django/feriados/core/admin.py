from django.contrib import admin
from .models import FeriadoModel
from datetime import date

class FeriadoModelAdmin(admin.ModelAdmin):
    list_display = ('nome','dia','mes','modificado_em','modificado_esse_mes')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome','dia','mes')
    list_filter = ('modificado_em',)
    
    def modificado_esse_mes(self, obj):
        hoje = date.today()
        return obj.modificado_em.month == hoje.month
    
    modificado_esse_mes.short_description = "Modificado esse mês"
    modificado_esse_mes.boolean = True
    
admin.site.register(FeriadoModel, FeriadoModelAdmin)
