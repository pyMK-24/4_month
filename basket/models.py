from django.db import models
from books.models import BookModel

class BasketModel(models.Model):
    STATUS_CHOICES = (
        ('Оплачено', 'Оплачено'),
        ('Не оплачено', 'Не оплачено'),
    )
    
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=200)
    description = models.TextField()
    choice_status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

