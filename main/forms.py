from django import forms
# Подключаем компонент UserCreationForm
from django.contrib.auth.forms import UserCreationForm
# Подключаем модель User
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.forms import BaseForm

from .models import *


# Создаём класс формы
class RegistrForm(UserCreationForm):
    # Добавляем новое поле Email
    email = forms.EmailField(max_length=254, help_text='This field is required')
    age = forms.IntegerField(help_text='This field is required')

    gender_choce = (
        ("definite", (("w", "woman"),
                      ("m", "man"),
                      )),
        ("indefinite", (("t", "trans"),
                        ("o", "other"),))
    )
    gender = forms.ChoiceField(choices=gender_choce, required=False)
    family_name = forms.CharField(max_length=255, required=False)
    amount_members = forms.IntegerField(required=False)
    abilities = forms.CharField(max_length=255, required=False)
    desease = forms.CharField(max_length=255, required=False)
    phobias = forms.CharField(max_length=255, required=False)
    languages = forms.CharField(max_length=255, required=False)
    vaccition = forms.CharField(max_length=255, required=False)
    phone = forms.CharField(max_length=255, required=False)

    def clean_age(self):
        if self.cleaned_data['age'] < 18:
            raise ValidationError('Нет 18 лет')
        return self.cleaned_data['age']

    # Создаём класс Meta
    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = (
            'username', 'email', 'age', 'gender', 'family_name', 'amount_members', 'abilities', 'desease', 'phobias',
            'languages', 'vaccition', 'phone', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit)
        Person.objects.create(
            **{
                'title': self.cleaned_data['username'],
                'family_name': self.cleaned_data['family_name'],
                'age': self.cleaned_data['age'],
                'gender': self.cleaned_data['gender'],
                'email': self.cleaned_data['email'],
                'amount_members': self.cleaned_data['amount_members'],
                'abilities': self.cleaned_data['abilities'],
                'desease': self.cleaned_data['desease'],
                'phobias': self.cleaned_data['phobias'],
                'languages': self.cleaned_data['languages'],
                'vaccition': self.cleaned_data['vaccition'],
                'phone': self.cleaned_data['phone'],
                'user': user
            })



class ContactForm(BaseForm):
    languages = forms.CharField(label='Имя (Необязательное поле)', max_length=255, required=False)
    vaccition = forms.EmailField(label='Email (Необязательное поле)', max_length=255, required=False)
    phone = forms.CharField(label='Опишите вашу проблему*', max_length=255, required=False)
