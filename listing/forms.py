from .models import Listing
from django import forms
from django.contrib.auth.models import User

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name','current_owner','price','agent','address','desc','image')
        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'current_owner' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.TextInput(attrs={'class':'form-control'}),
            'desc' : forms.Textarea(attrs={'class':'form-control'}),
            'address' : forms.Textarea(attrs={'class':'form-control'}),
        }
