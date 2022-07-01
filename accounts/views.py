from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Conta {user} criada com sucesso')
                return redirect('login')

        context = {
            'form': form,
        }
        return render(request, 'registration/register.html', context)
