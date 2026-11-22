from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Customer

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    middle_initial = forms.CharField(max_length=1)
    last_name = forms.CharField(max_length=255)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    field_order = ['first_name', 'middle_initial', 'last_name', 'birth_date', 'password1', 'password2']

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ()

    def save(self):
        customer = Customer.objects.create(
            first_name=self.cleaned_data['first_name'],
            middle_initial=self.cleaned_data['middle_initial'],
            last_name=self.cleaned_data['last_name'],
            birth_date=self.cleaned_data['birth_date'],
        )
        customer.user = User.objects.create_user(
            username=str(customer.customer_id),
            password=self.cleaned_data['password1'],
        )
        customer.save()
        return customer

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Customer ID') # changes label from username to Customer ID