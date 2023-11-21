from .models import Person, Rank
from django.forms import ModelForm, TextInput,  DateInput
from django import forms


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ["Surname", "Name", "Middlename", "Employed", "rank"]
        widgets = {
            "Surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "Name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "Middlename": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите отчество'
            }),
            "Employed": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату YYYY-MM-DD'
            }),
            "rank": forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Выберите должность'
            })


        }


class RankForm(ModelForm):
    class Meta:
        model = Rank
        fields = ["Rank"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите должность'
            })

        }
