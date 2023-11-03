from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=15,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Номер телефона')
    birth_date = forms.CharField(required=True,widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}),label='Дата рождения')
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES,required=True,widget=forms.Select(attrs={'class': 'form-select'}),label='Пол')
    image = forms.ImageField(required=True,widget=forms.FileInput(attrs={'class': 'form-control'}),label='Фотография')
    password1 = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
    password2 = forms.CharField(label="Подтверждение пароля",widget=forms.PasswordInput(attrs={'class': 'form-control'}),)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'phone', 'birth_date' , 'gender', 'image', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
        }
