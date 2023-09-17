from django import forms
from app1.models import *

class booking_detail2(forms.ModelForm):
    class Meta:
        model=booking_detail
        fields='__all__'
    
