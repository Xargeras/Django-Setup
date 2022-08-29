from django import forms
from django.contrib.auth.backends import UserModel

from myapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created', 'user']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomName',
                'placeholder': "Имя товара",
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomDescription',
                'placeholder': "Описание товара",
            }),
            'price': forms.NumberInput({
                'class': 'form-control',
                'id': 'validationCustomPrice',
                'placeholder': "Цена товара",
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomAmount',
                'placeholder': "Количество товара",
            })
        }


class UserSettings(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomUsername',
                'placeholder': "Имя пользователя",
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustom01',
                'placeholder': "Имя",
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustom02',
                'placeholder': "Фамилия",
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomEmail',
                'placeholder': "E-mail",
            }),
        }
