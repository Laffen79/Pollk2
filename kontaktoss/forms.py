from django import forms
from .models import KontaktMelding

class KontaktSkjema(forms.ModelForm):
    class Meta:
        model = KontaktMelding
        fields = ['navn', 'epost', 'melding']
