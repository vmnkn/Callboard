from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
        widgets = {
            'username': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
            'email': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
            'password1': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
            'password2': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
