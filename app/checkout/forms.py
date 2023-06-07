from django import forms

from checkout.models import UserEstimate

class UserEstimateForm(forms.ModelForm):
    
    class Meta:
        model = UserEstimate
        fiels = "__all__"