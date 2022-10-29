from django import forms


class Calculator(forms.Form):
    number_one = forms.IntegerField()
    number_two = forms.IntegerField()
