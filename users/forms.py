from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (
        ('М','Мужской'),
        ('Ж','Женский')
)
JOB_TITLE = (
    ('Lead', 'Ведущий разработчик'),
    ('Tech Lead', 'Технический лидер'),
    ('Architect', 'Архитектор программного обеспечения'),
    ('DevOps', 'Инженер DevOps'),
    ('QA', 'Тестировщик'),
    ('Fullstack', 'Fullstack разработчик'),
    ('Frontend', 'Frontend разработчик'),
    ('Backend', 'Backend разработчик'),
    ('Data Scientist', 'Дата-сайентист'),
    ('Machine Learning Engineer', 'Инженер машинного обучения'),
    ('iOS Developer', 'Разработчик iOS'),
    ('Android Developer', 'Разработчик Android'),
    ('Embedded Developer', 'Разработчик встроенных систем'),
)
    
class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Впишите свой email адрес')
    phone = forms.CharField(required=True, label='Введите ваш номер телефона')
    age = forms.IntegerField(required=True)
    year = forms.IntegerField(required=True, label='Введите ваш опыт работы')
    gender = forms.ChoiceField(choices=GENDER, label='Укажите ваш пол')
    about_me = forms.CharField(required=True, max_length=1500)
    job_title = forms.ChoiceField(choices=JOB_TITLE,label='Укажите свою специальность')
    
    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'phone',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'about_me',
            'year',
            'job_title',
        )
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']  
        user.age = self.cleaned_data['age']
        user.year = self.cleaned_data['year']
        user.gender = self.cleaned_data['gender']
        user.about_me = self.cleaned_data['about_me']
        user.job_title = self.cleaned_data['job_title']
        
        if commit:
            user.save()
        return user
    