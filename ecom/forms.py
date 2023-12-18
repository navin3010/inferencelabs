from django import forms
from ecom.models import Review


class ContactForm(forms.Form):
    class Meta:
        model = Review
    products = forms.IntegerField(required=True)
    rating = forms.CharField(required=True)
    pros = forms.CharField(required=True)
    crons = forms.CharField(required=True)
    review = forms.CharField(widget=forms.Textarea)
    fields = ["rating"]