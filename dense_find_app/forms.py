from django import forms


class TextForm(forms.Form):
    coordinates = forms.CharField()
