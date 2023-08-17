from django.contrib.auth import forms
from .models import CustomUser
from .models import HealthInfo
from django import forms

#from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'name', 'password1', 'password2', 'age', 'email', 'image', 'gender', 'phone_number']
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()     
        fields = ['username', 'name', 'age', 'email', 'image', 'gender', 'phone_number']
        
class HealthInfoForm(forms.ModelForm):
    class Meta:
        model = HealthInfo
        fields = ['height', 'weight', 'medical_history']