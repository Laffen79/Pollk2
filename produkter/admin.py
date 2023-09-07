from django.contrib import admin
from .models import Propanflaske

class PropanflaskeAdmin(admin.ModelAdmin):
    list_display = ('artikkelnummer_nykjop', 'artikkelnummer_fylling', 'NOBB_nykjop', 'NOBB_fylling','beskrivelse', 'materiale', 'ventil', 'diameter', 'hoyde', 'gassmengde', 'taravekt', 'totalvekt', 'bilde_id')

admin.site.register(Propanflaske, PropanflaskeAdmin)
