from django import forms

from home.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Name of the product'}),
            'description': forms.Textarea(attrs={'class': 'form_control', 'placeholder': "description"}),
            'price': forms.NumberInput(attrs={'class': 'form_control', 'placeholder': 'price Of the product'}),
            'category': forms.Select(attrs={'class': 'form_control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form_control'}),
            # 'available': forms.BooleanInput(attrs={'class':'form_control', 'placeholder': 'available' }),
            'stock': forms.NumberInput(attrs={'class': 'form_product', 'placeholder': 'Stock'})

        }
