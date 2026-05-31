from django.shortcuts import render, redirect

from django.contrib.auth import (

    login,
    logout,
    authenticate

)

from .forms import (

    RegisterForm,
    LoginForm

)

from comptes.decorators import role_required


@role_required(['admin'])
def dashboard_admin(request):

    return render(
        request,
        'dashboard.html'
    )

def register_view(request):

    form = RegisterForm(
        request.POST or None
    )

    if form.is_valid():

        user = form.save()

        login(request, user)

        return redirect('/')

    return render(

        request,

        'comptes/register.html',

        {

            'form': form

        }

    )


def login_view(request):

    form = LoginForm(
        request,
        data=request.POST or None
    )

    if form.is_valid():

        user = form.get_user()

        login(request, user)

        return redirect('/')

    return render(

        request,

        'comptes/login.html',

        {

            'form': form

        }

    )


def logout_view(request):

    logout(request)

    return redirect('home')