from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError

def register_view(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return redirect('security:register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está en uso.")
            return redirect('security:register')

        # Create the new user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            # Authenticate and log the user in after registration
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your home view name

            messages.success(request, "Cuenta creada exitosamente.")
            return redirect(reverse('security:login'))

        except ValidationError as e:
            messages.error(request, f"Error en el formulario: {e}")
            return redirect('security:register')

    return render(request, 'register.html')
