from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'register.html', args)
