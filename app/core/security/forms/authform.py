from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from core.security.models import User

class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=10, required=False, label="Número de teléfono")
    address = forms.CharField(max_length=255, required=False, label="Dirección")
    date_of_birth = forms.DateField(required=False, label="Fecha de nacimiento")
    profile_image = forms.ImageField(required=False, label="Imagen de perfil")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'address', 'date_of_birth', 'profile_image']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        return username

class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        # Agregar depuración aquí
        print("Verificando usuario:", username)  # Imprime el nombre de usuario recibido
        print("Contraseña proporcionada:", password)  # Imprime la contraseña proporcionada

        if not username or not password:
            raise forms.ValidationError("Este campo es obligatorio.")

        # Verificación de autenticación
        user = authenticate(username=username, password=password)

        # Depuración del resultado de autenticación
        if user is None:
            print("Autenticación fallida para:", username)  # Si el usuario es None, imprime el fallo
            raise forms.ValidationError("Nombre de usuario o contraseña incorrectos.")

        cleaned_data["user"] = user
        return cleaned_data
