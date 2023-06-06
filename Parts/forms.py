from django import forms

from Parts.models import Customer, Part


class PartForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control rounded-0', 'placeholder': 'Zákazník'}))

    class Meta:
        model = Part
        fields = '__all__'
        widgets = {
            'customer_part': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Cislo dielu'}),
            'revision': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Revizia'}),
            'description': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Popis'}),
        }

