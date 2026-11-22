from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            customer = form.save()
            messages.success(
                request,
                f'Registered Successfully. Your Customer ID is {customer.customer_id}. Use it to log in.',
            )
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})