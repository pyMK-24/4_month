from django.db import models
from books.models import BookModel

class TodoModel(models.Model):
    STATUS_CHOICES = (
        ('Посмотрел','Посмотрел'),
        ('Не посмотрел','Не посмотрел'),
    )
    task = models.CharField(max_length=100)
    choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    choice_status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task
