from django.shortcuts import render
from .models import Propanflaske

def propanflasker_liste(request):
    propanflasker = Propanflaske.objects.all()
    return render(request, 'produkter/propanflasker_liste.html', {'propanflasker': propanflasker})

def propanflaske_detail(request, NOBB_nykjop):
    propanflaske = Propanflaske.objects.get(NOBB_nykjop=NOBB_nykjop)
    return render(request, 'produkter/propanflaske_detail.html', {'propanflaske': propanflaske})
