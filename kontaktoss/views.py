from django.shortcuts import render, redirect
from .forms import KontaktSkjema
from django.core.mail import send_mail
from django.conf import settings

def kontakt_oss(request):
    if request.method == 'POST':
        skjema = KontaktSkjema(request.POST)
        if skjema.is_valid():
            skjema.save()
            navn = skjema.cleaned_data['navn']
            epost = skjema.cleaned_data['epost']
            melding = skjema.cleaned_data['melding']
            
            # Send e-post
            emne = 'Kontaktforespørsel fra nettstedet'
            melding_tekst = f'Navn: {navn}\nE-post: {epost}\n\nMelding:\n{melding}'
            send_mail(emne, melding_tekst, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])


            return redirect('kontakt_oss')  # Bytt 'kontakt_oss' med navnet på URL-en for Kontakt oss siden
    else:
        skjema = KontaktSkjema()

    return render(request, 'kontaktoss/kontakt_oss.html', {'skjema': skjema})
