from django import forms

from Customers.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Meno'}),
        }
