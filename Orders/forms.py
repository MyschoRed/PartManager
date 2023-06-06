from django import forms

from Orders.models import Customer, Part, Order


class OrderForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control rounded-0', 'placeholder': 'Zakaznik'}))
    part = forms.ModelChoiceField(queryset=Part.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control rounded-0', 'placeholder': 'Diel'}))

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'pcs': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Pocet kusov'}),
        }
