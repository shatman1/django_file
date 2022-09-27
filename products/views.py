from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'name': '''I'm Shatman''',
        'age': '''I'm 27 yers old''',
        'aboutme': '''О себе''',
        'lorem': '''Я Буларов Шатман мне 27 лет. я учусь на курсы Python''',
        'Search': '''Где меня найти''',
        'Bootstrap': '''Ссылка на сайт''',

    }
    return render(request, 'main.html', data)


def test(request):
    datas = [
        {'deal': 'Action deal 1',
        'img': 'https://www.undp.org/sites/g/files/zskgke326/files/migration/cn/UNDP-CH-Why-Humanity-Must-Save-Nature-To-Save-Itself.jpeg',
        'cash_back': 'buy 3 and get 1 free'},
        {'deal': 'Action deal 1',
         'img': 'https://www.undp.org/sites/g/files/zskgke326/files/migration/cn/UNDP-CH-Why-Humanity-Must-Save-Nature-To-Save-Itself.jpeg',
         'cash_back': 'buy 3 and get 1 free'},
        {'deal': 'Action deal 1',
         'img': 'https://www.undp.org/sites/g/files/zskgke326/files/migration/cn/UNDP-CH-Why-Humanity-Must-Save-Nature-To-Save-Itself.jpeg',
         'cash_back': 'buy 3 and get 1 free'},
        {'deal': 'Action deal 1',
         'img': 'https://www.undp.org/sites/g/files/zskgke326/files/migration/cn/UNDP-CH-Why-Humanity-Must-Save-Nature-To-Save-Itself.jpeg',
         'cash_back': 'buy 3 and get 1 free'},
        {'deal': 'Action deal 1',
         'img': 'https://www.undp.org/sites/g/files/zskgke326/files/migration/cn/UNDP-CH-Why-Humanity-Must-Save-Nature-To-Save-Itself.jpeg',
         'cash_back': 'buy 3 and get 1 free'},
        {'deal': 'Action deal 1',
         'img': 'https://www.undp.org/sites/g/files/zskgke326/files/migration/cn/UNDP-CH-Why-Humanity-Must-Save-Nature-To-Save-Itself.jpeg',
         'cash_back': 'buy 3 and get 1 free'},


    ]

    return render(request, 'test_jinja.html', {'data': datas})

def repetit(request):
    data = [{'deal': 'Action deal1',
            'img': 'https://kartinkin.net/uploads/posts/2022-03/thumbs/1646877870_6-kartinkin-net-p-kartinki-shoping-6.jpg',
            'cash_back': 'Buy 4 and get 1 free'},
            {'deal': 'Action deal2',
            'img': 'https://kartinkin.net/uploads/posts/2022-03/thumbs/1646877870_6-kartinkin-net-p-kartinki-shoping-6.jpg',
            'cash_back': 'Buy 4 and get 1 free'},

    ]
    return render(request, 'repetition.html', data)


def my_list(request):
    return HttpResponse('И во второго раза')


def practice(request):
    return HttpResponse('hello')


def pris(request):
    return HttpResponse('сентябрь')


def file(request):
    return HttpResponse('Document')


def address(request):
    return HttpResponse('Django')
