from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class LoginForm(forms.Form):
    username = forms.CharField(label= "Username")
    password = forms.CharField(label= "Password", widget= forms.PasswordInput)


class RegisterForm(forms.Form):      # burada UserCreationForm kullaninca otomatik form olusturur dolayisiyla password kismini cikarabiliriz. Ama forms.Form kullanirsak eklemek zorundayiz 
    username = forms.CharField(max_length= 50, label= "Username")
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(max_length= 20, label= "Password", widget= forms.PasswordInput)
    confirm = forms.CharField(max_length= 20, label= "Password Confirmation", widget= forms.PasswordInput)
    

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords does not match!")


        values = {
            "username": username,
            'email':email,
            "password": password,
        }
        return values


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'username',
            'password'
        )
        


