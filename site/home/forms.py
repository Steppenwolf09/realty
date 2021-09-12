from .models import House
from django.forms import ModelForm, TextInput, NumberInput, RadioSelect
from django import forms

class Auth(ModelForm):
    


class HouseForm(ModelForm):



    class Meta:
        model=House
        fields=["name", "descrip", "kol_rooms", "price", "square", "square_of_area","commission","aim", "adress"]


        widgets = {
            "name":TextInput(attrs={
               "class":"form-control",

               "placeholder":"Наименование"
        }),
            "descrip": TextInput(attrs={
                "class": "form-control",

                "placeholder": "Описание"
            }),

            "adress": TextInput(attrs={
                "class": "form-control",

                "placeholder": "Адрес"
            }),

            "kol_rooms": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Комнаты"
            }),
            "price": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Цена"
            }),



            "square": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Площадь (кв.м.)"
            }),

            "square_of_area": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Площадь (кв.м.)"
            }),


            "commission": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Комиссия (руб.)"
            }),
            "aim": RadioSelect(attrs={
                "name":"aim",
                "class": "form-control",
                "placeholder": "Цель"
            })

        }




