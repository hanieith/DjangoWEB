from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя',
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=150, label='Пароль',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(max_length=150, label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(max_length=150, label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Почтовый адрес', widget= forms.EmailInput(attrs={"class": "form-control"}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# class NewsForm(forms.Form):
# title = forms.CharField(max_length=150, label='Название',  widget=forms.TextInput(attrs={"class": "form-control"}))
# content = forms.CharField(label='Содержание новости', required=False,
# widget=forms.Textarea(attrs={"class": "form-control", "rows":5}))
# is_published = forms.BooleanField(label='Опубликовано', initial=True, )
# category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
# empty_label='Выберите категорию', widget=forms.Select(attrs={"class": "form-control"}))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {'title': forms.TextInput(attrs={"class": "form-control"}),
                   'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
                   'category': forms.Select(attrs={"class": "form-control"})}

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должны идти с цифры')
        return title
