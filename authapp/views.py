from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import FoxUserLoginForm, FoxUserRegisterForm, FoxUserEditForm
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages
from main.views import get_shops_menu


def login(request):
    title = 'Личный кабинет | edaFox'
    shops = get_shops_menu()

    login_form = FoxUserLoginForm(data=request.POST or None)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))

    content = {'title': title, 'login_form': login_form, 'shops': shops}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    title = 'Регистрация | edaFox'
    shops = get_shops_menu()

    if request.method == 'POST':
        register_form = FoxUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = FoxUserRegisterForm()

    content = {'title': title, 'register_form': register_form, 'shops': shops}
    return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'Редактирование профиля | edaFox'
    shops = get_shops_menu()

    if request.method == 'POST':
        edit_form = FoxUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = FoxUserEditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form, 'shops': shops}
    return render(request, 'authapp/edit.html', content)


def change_password(request):
    title = 'Смена пароля | edaFox'
    shops = get_shops_menu()

    if request.method == 'POST':
        change_password_form = PasswordChangeForm(request.user, request.POST)
        if change_password_form.is_valid():
            user = change_password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('auth:edit'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        change_password_form = PasswordChangeForm(request.user)

    content = {'title': title, 'change_password_form': change_password_form, 'shops': shops}
    return render(request, 'authapp/change_password.html', content)
