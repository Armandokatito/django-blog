from django import forms
from userprofile.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('likes_cheese','favourite_hamster_name')