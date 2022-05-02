import re
from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import *


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')

class UserForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="confirm password")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class sellerForm(forms.ModelForm):
    class Meta:
        model = seller
        exclude = ('user',)
        fields = ('Name', 'Phone_no', 'Address')

Gender_choice = (
    ("male","male"),
    ("female","female")
)


class customerForm(forms.ModelForm):
    Gender = forms.ChoiceField(choices=Gender_choice,required=True,widget=forms.RadioSelect)
    Phone_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = customer
        exclude = ('user',)
        fields = ('Name', 'Phone_no', 'Address','Gender')

class AddpetForm(forms.ModelForm):
    class Meta:
        model = pet
        fields = ('title', 'price', 'category','description','picture')
        widget ={
            'picture':forms.FileInput(attrs={'class':'form-control'}),
        }

class orderForm(forms.ModelForm):
    class Meta:
        model = orderplaced
        fields = ('title', 'price', 'category','description','picture')

class DateInput(forms.DateInput):
    input_type = 'date'


class payment_Form(forms.ModelForm):
    class Meta:
        model = payment
        fields = ('shipping_address','price','card_number','cvv','date')

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Invalid Date")
        return date



