from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Platform'
    }
    return render(request, 'fourth_task/index.html', context)


def store(request):
    context = {
        'title': 'Game_Store',
        'list': ['Dota2', 'GTA5',
                 'BloodStrike', 'Fallout4'],
        'button': 'купить'
    }
    return render(request, 'fourth_task/store.html', context)


def cart(request):
    context = {
        'title': 'Cart',
        'content': 'Извините, ваша корзина пуста. Чтобы добавить товары '
                   'нажмите кнопку КУПИТЬ в магазине'
    }
    return render(request, 'fourth_task/cart.html', context)
