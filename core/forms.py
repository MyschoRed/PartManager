from django import forms

from core.models import Customer, Part


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Meno'}),
            'boost_id': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Boost ID'}),
        }



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
