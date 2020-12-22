from django.contrib import admin
from .models import Autor, Libro, Contacto

# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "autor"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["autor"]

admin.site.register(Autor)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Contacto)