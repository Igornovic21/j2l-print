from django import forms

from checkout.models import UserEstimate

class UserEstimateForm(forms.ModelForm):
    
    class Meta:
        model = UserEstimate
        fields = ['first_name', 'last_name', 'email', 'organisation', 'phone', 'address', 'postal_code', 'city', 'message']