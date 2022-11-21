from django.contrib import admin
from imobiliariaSA.models import Categoria, TipoImovel, Imovel, Pessoa, FotoImovel
from nested_inline.admin import NestedTabularInline, NestedModelAdmin

class FotosInLine(NestedTabularInline):
    model = FotoImovel
    extra = 0


class ImovelAdmin(NestedModelAdmin):
    inlines = [FotosInLine]

admin.site.register(Categoria)
admin.site.register(TipoImovel)
admin.site.register(Imovel, ImovelAdmin)
#admin.site.register(FotoImovel)
admin.site.register(Pessoa)
