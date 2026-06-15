from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import NameForm
from .models import UserName

def home(request):
    name = request.GET.get('name', None)
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user_name = form.save()
            name = user_name.name.capitalize()
            # messages.success(request, f'Добро пожаловать, {name}!')
            return redirect(f"/?name={name}")
        else:
            messages.error(request, 'Пожалуйста, введите корректное имя.')
            name = None
    else:
        messages.success(request, f'Введите ваше имя, чтобы получить персональное приветствие')
        form = NameForm()

    context = {
        'form': form,
        'name': name,
        'all_names': UserName.objects.all().order_by('-id')[:10]  # последние 10 имён
    }
    return render(request, 'greetings/home.html', context)
