from django.db import models
from django.contrib.auth.models import User

junior_delevoper = 'начинающего разработчика.Заработная плата:500-1000$'
middle_delevoper = 'среднего разработчика.Заработная плата:1000-2000$'
senior_delevoper = 'старшего разработчика.Заработная плата:2000-3000$'

class CustomUser(User):
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

    phone_number = models.CharField(max_length=14, default='+996')
    year = models.PositiveIntegerField(default=1)
    gender = models.CharField(max_length=1,choices=GENDER,default='M')
    job_title = models.CharField(max_length=100,choices=JOB_TITLE,default='Lead')
    position = models.CharField(max_length=100)
    about_me = models.CharField(max_length=1500, blank=True)  
    age = models.PositiveIntegerField(default=18) 
    
    def save(self, *args, **kwargs):
        if self.year < 1:
            self.year = 'Ваш год работы не может быть меньше 1'
        elif 1 <= self.year < 3:
            self.position = junior_delevoper
        elif 3 <= self.year < 8:
            self.position = middle_delevoper
        elif 8 <= self.year < 15:
            self.position = senior_delevoper
        else:
            self.position = 'Вы профессионал в этом деле.Вы выше все этого :)'
        super().save(*args, **kwargs)
            