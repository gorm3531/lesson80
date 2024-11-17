from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
# Create your views here.


def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        password_rep = request.POST.get('password_rep')
        age = int(request.POST.get('age'))
        if login in users:
            info['error'] = f'Пользователь {login} уже существует'
        if password != password_rep:
            info['error'] = 'Пароли не совпадают'
        if age < 18:
            info['error'] = 'Вы должны быть старше 18'
        if info:
            return render(request, 'fifth_task/registration_page.html', context=info)
        return HttpResponse(f'Приветствуем {login}')
    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            password_rep = form.cleaned_data['password_rep']
            age = int(form.cleaned_data['age'])
            if login in users:
                info['error'] = f'Пользователь {login} уже существует'
            if password != password_rep:
                info['error'] = 'Пароли не совпадают'
            if age < 18:
                info['error'] = 'Вы должны быть старше 18'
            if info:
                return render(request, 'fifth_task/registration_page.html', context=info)
            return HttpResponse(f'Приветствуем {login}')
    form = RegistrationForm()
    return render(request, 'fifth_task/registration_page.html', {'form': form})