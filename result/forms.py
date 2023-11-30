from django import forms
from .models import LGA, AnnouncedPuResult


class LgaForm(forms.Form):
    lga = forms.ModelChoiceField(queryset=LGA.objects.all())


class AddResultForm(forms.ModelForm):
    class Meta:
        model = AnnouncedPuResult
        fields = '__all__'
