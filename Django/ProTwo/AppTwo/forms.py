from django import forms
from AppTwo.models import User

# Linking a form to a model
class NewUserForm(forms.ModelForm):
    # Custom validations go in between

    class Meta:
        model = User
        fields = '__all__' # For all fields
