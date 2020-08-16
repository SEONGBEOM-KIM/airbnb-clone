from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # for validation(is_valid), "clean_" 뒤에 위의 폼 변수

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is worng"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(UserCreationForm):

    username = forms.EmailField(label="Email")
