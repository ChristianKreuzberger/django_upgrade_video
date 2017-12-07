from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class LoginForm(forms.Form):
    """
    ToDo: Implement a login form with username and password
    """
    pass


class RegistrationForm(forms.ModelForm):
    """
    Provides a registration form
    """
    username = forms.CharField()

    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput(), label=_("Password")
    )

    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(), label=_("Password (again)")
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )

    def clean_email(self):
        """
        Verify that a user with a similar email address does not exist yet
        :return:
        """
        try:
            user = User.objets.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']

        raise forms.ValidationError(_("A user with the specified email address already exists. Please try another one."))

    def clean_username(self):
        """
        Verify that a user with a similar username does not exist yet
        :return:
        """
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']

        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        """
        Verify that the provided passwords are the same
        :return:
        """
        if 'password' in self.cleaned_data and 'password_confirmation' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_confirmation']:
                raise forms.ValidationError(_("The two password fields did not match."))

        return self.cleaned_data
