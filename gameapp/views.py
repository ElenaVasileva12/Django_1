from django.shortcuts import render
from django.http import HttpResponse
from random import *
# Create your views here.

# � Создайте представление “Привет, мир!” внутри вашего
# первого приложения
def index(request):
    return HttpResponse('Привет, мир!')

# � Создайте новое приложение. Подключите его к проекту. В
# приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# � Орёл или решка
# � Значение одной из шести граней игрального кубика
# � Случайное число от 0 до 100
def orel_resko(request):
    return HttpResponse(choice(['Орел','Решка']))

def cub(request):
    return HttpResponse(str(randint(1,7)))

def numbers(request):
    return HttpResponse(str(randint(1,101)))
