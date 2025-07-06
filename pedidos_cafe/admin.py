from django.contrib import admin
from pedidos_cafe.models import PedidoCafe
from pedidos_cafe.forms import PedidoCafeAdminForm 


@admin.register(PedidoCafe) 
class PedidoCafeAdmin(admin.ModelAdmin):
    form = PedidoCafeAdminForm 

    list_display = ('cliente', 'tipo_base', 'tamanio', 'fecha', 'ingredientes_display')
    
    def ingredientes_display(self, obj):
        return ", ".join(obj.ingredientes)
    ingredientes_display.short_description = "Ingredientes"
