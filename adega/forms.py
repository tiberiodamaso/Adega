from django import forms
from .models import Adega


class AdegaForm(forms.ModelForm):

    class Meta:
        model = Adega
        fields = ['nome', 'qtd_vinhos', 'ativa']