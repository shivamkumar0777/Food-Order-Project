from django import forms

from .models import Food


class CheckoutForm(forms.Form):
    customer_name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'Your full name'}),
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Phone number'}),
    )
    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 4,
                'placeholder': 'Delivery address',
            }
        )
    )


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Food name'}),
            'description': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Short description',
                }
            ),
            'price': forms.NumberInput(attrs={'placeholder': 'Price in rupees'}),
            'image': forms.TextInput(attrs={'placeholder': 'Image URL or /static/... path'}),
        }
