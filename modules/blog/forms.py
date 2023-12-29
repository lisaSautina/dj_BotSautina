from django import forms

class Sending(forms.Form):
    message = forms.CharField(widget = forms.Textarea, label = "Sending" )