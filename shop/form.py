from cgi import print_exception
from django import forms


class Food_form(forms.Form):
    name = forms.CharField(max_length = 30)
    mark = forms.CharField(max_length = 30)
    size = forms.CharField(max_length = 30)
    type = forms.CharField(max_length = 30)
    price = forms.CharField(max_length = 30)

class Toys_form(forms.Form):
    name = forms.CharField(max_length = 30)
    mark = forms.CharField(max_length = 30)
    size = forms.CharField(max_length = 30)
    type = forms.CharField(max_length = 30)
    price = forms.CharField(max_length = 30)

class Vet_form(forms.Form):
    name = forms.CharField(max_length = 30)
    mark = forms.CharField(max_length = 30)
    size = forms.CharField(max_length = 30)
    type = forms.CharField(max_length = 30)
    price = forms.CharField(max_length = 30)

