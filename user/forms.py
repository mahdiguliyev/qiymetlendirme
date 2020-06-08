from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class LoginForm(forms.Form):
    fin = forms.CharField(label="Fin")
    password = forms.CharField(label="Parol", widget=forms.PasswordInput)

class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)
    confirm = forms.CharField(label='Parolu təstiqlə', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('fin', 'username', 'sirname', 'email')

    def clean_confirm(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Parol bir-birinə uyğun deyil!")
        return confirm

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('fin', 'username', 'sirname', 'email', 'password', 'active', 'company_user', 'customer_user', 'admin')

    def clean_password(self):

        return self.initial["password"]