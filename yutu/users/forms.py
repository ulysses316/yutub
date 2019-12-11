from django import forms
from users.models import Users

class UserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
           # "age",
            "image_profile"
        ]

        labels = {
            "username": "Nombre de usuario", 
            "password": "Contraseña",
            "email": "Correo electronico",
            "first_name": "Nombres",
            "last_name": "Apellidos",
           # "age":"Edad",
            "image_profile": "Imagen de perfil"
        }

        widgets = {
            "username": forms.TextInput(attrs={'class':"input-field"}),
            "password": forms.PasswordInput(),
            "email": forms.EmailInput(attrs={'class':"input-field"}),
            "first_name": forms.TextInput(attrs={'class':"input-field"}),
            "last_name": forms.TextInput(attrs={'class':"input-field"}),
           # "age": forms.DateInput(attrs={'class':"input-field"}),
            "image_profile": forms.ClearableFileInput(attrs={'class':["file-path","validate"]})
        }