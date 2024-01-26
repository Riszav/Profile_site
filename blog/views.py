from django.shortcuts import render, redirect
from .models import Cars
from django.contrib.auth import authenticate, login, logout
from user.forms import RegisterForm, LoginForm

# # Create your views here.
# if request.method == 'GET':
#     context = {
#         'form': LoginForm,
#     }
#     # print(request.user) # request.user - объект пользователя, который сделал запрос
#     return render(request, 'user/login.html', context=context)
#
# elif request.method == 'POST':
#     form = LoginForm(request.POST)
#
#     if form.is_valid():
#         user = authenticate(**form.cleaned_data)  # метод который проверяет есть ли такой пользователь в базе данных
#
#         if user is not None:
#             login(request, user)  # метод который авторизует пользователя (создает сессию)
#             return redirect('/posts/')
#
#         else:
#             form.add_error(
#                 None,
#                 'Пользователь с такими данными не найден!'
#             )
#
#     return render(request, 'user/login.html', context={'form': form})
def main_view(request):
    if request.method == 'GET':
        # 1 - получить все хэштеги из базы данных
        cars = Cars.objects.all()
        cars = cars.order_by('-created_at')
        limit = 4

        # 2 - передать хэштеги в шаблон
        context = {
            'cars': cars[0:limit],
            'form': LoginForm,
            'user': request.user
        }

        # 3 - вернуть ответ с шаблоном и данными

        return render(request, 'index.html', context=context)

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(**form.cleaned_data)  # метод который проверяет есть ли такой пользователь в базе данных

            if user is not None:
                login(request, user=user)  # метод который авторизует пользователя (создает сессию)
                return redirect('/')

            else:
                form.add_error(
                    None,
                    'Пользователь с такими данными не найден!'
                )

        return render(request, 'index.html', context={'form': form})