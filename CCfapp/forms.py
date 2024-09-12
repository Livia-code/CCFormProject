from django import forms
from . models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerForm
        fields = "__all__"