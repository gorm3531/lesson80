from django.shortcuts import render


# Create your views here.


def index(request):
    context = {
        'title': 'Platform',
        'heading': 'Главная страница',
        'link1': 'Главная',
        'link2': 'Магазин',
        'link3': 'Корзина',
    }
    return render(request, 'third_task/index.html', context)


def store(request):
    context = {
        'title': 'Game_Store',
        'headind': 'Игры',
        'button': 'Купить',
    }
    return render(request, 'third_task/store.html', context)


def cart(request):
    context = {
        'title': 'cart',
        'heading': 'Корзина',
        'content': 'Извините, ваша корзина пуста. Чтобы добавить товары '
                   'нажмите кнопку КУПИТЬ в магазине'
    }
    return render(request, 'third_task/cart.html', context)
