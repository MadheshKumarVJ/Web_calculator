from email.policy import default
from django import forms


class Calculator(forms.Form):
    number_one = forms.IntegerField()
    number_two = forms.IntegerField()
    CHOICES = [("add", "Add"), ("sub", "Sub"), ("mul", "Mul"), ("div", "Div")]
    operation = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
