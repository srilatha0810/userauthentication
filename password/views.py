from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'your password was successfully updated')
            return redirect('/password')
          
        else:
            messages.error(request, 'please correct the error below')

    else:
        form = PasswordChangeForm(request.user)
    return render(request,'change_password.html', {'form': form})