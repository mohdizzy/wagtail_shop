from allauth.account.forms import SignupForm
from bakery.models import Profile
from django import forms
from django.contrib.auth.models import User



class CustomSignupForm(SignupForm):

    first_name = forms.CharField(max_length=30, label='First Name',required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=30, label='Last Name',required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    phone = forms.CharField(max_length=10, min_length=10, required=True,
                        widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))


    def clean_phone(self):
        cleaned_data = self.cleaned_data['phone']
        if cleaned_data.isdigit():
            return cleaned_data
        else:
            raise forms.ValidationError("Enter a valid 10 digit phone number")


    def save(self, request):

        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        up = user.profile
        up.phone = self.cleaned_data['phone']
        user.save()
        up.save()
        return user


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('phone',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self['phone'].initial = ''

    def clean_phone(self):
        cleaned_data = self.cleaned_data['phone']

        if cleaned_data.isdigit():
            return cleaned_data
        else:
            raise forms.ValidationError('Enter valid 10 digit number')


    def save(self, user=None):
        user = super(ProfileForm, self).save(commit=False)

        user.phone = self.cleaned_data['phone']
        user.save()

        return user

class NameForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name',)

    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        self['first_name'].initial = ''

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name == '':
            raise forms.ValidationError("This field is required.")
        return first_name

    def save(self, commit=True):
        user = super(NameForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.save()

        return user

