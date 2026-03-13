from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import NameForm
from .models import UserName

def home(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user_name = form.save()
            messages.success(request, f'Добро пожаловать, {user_name.name}!')
            return redirect('/')
        else:
            messages.error(request, 'Пожалуйста, введите корректное имя.')
    else:
        form = NameForm()

    # Получаем последнее сохранённое имя (или None, если записей нет)
    last_name = UserName.objects.last()

    context = {
        'form': form,
        'last_name': last_name,
        'all_names': UserName.objects.all().order_by('-id')[:10]  # последние 10 имён
    }
    return render(request, 'greetings/home.html', context)
