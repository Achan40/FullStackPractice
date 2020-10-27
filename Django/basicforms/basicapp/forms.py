from django import forms
from django.core import validators

# custom validator using django module
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with Z")

class FormName(forms.Form):
    # using custom validator
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter Your Email Again ')
    text = forms.CharField(widget=forms.Textarea)
    
    # Catching bots
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    # Clean form data, verify email
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails match")

    # custom Validator
    # def clean_botcatcher(self):
        #botcatcher = self.cleaned_data['botcatcher']
        #if len(botcatcher) > 0:
            #raise forms.ValidationError("Got a bot!")
        #return botcatcher

    # Django Built in Validators use validators module