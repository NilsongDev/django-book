# registro/views.py
from django.shortcuts import render, redirect
from .form import UserRegistrationForm

def registro_usuario(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes agregar la lógica para guardar el usuario o redirigir
            return redirect('success')  # Redirige a una página de éxito
    else:
        form = UserRegistrationForm()
    return render(request, 'registro/registro_usuario.html', {'form': form})
