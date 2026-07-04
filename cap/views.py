from django.shortcuts import render, redirect
from .forms import StudentForm


def register(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('register')

    else:

        form = StudentForm()

    return render(
        request,
        "college/register.html",
        {'form':form}
    )


def login(request):

    return render(
        request,
        "college/login.html"
    )