from django.db import models

class BookModel(models.Model):
    GENRE_CHOICES = (
    ('FANTASY', 'FANTASY'),
    ('DRAMA', 'DRAMA'),
    ('MYSTERY', 'MYSTERY'),
    ('ADVENTURE', 'ADVENTURE'),
    ('DETECTIVE', 'DETECTIVE'),
    ('ROMANCE', 'ROMANCE'),
    ('HORROR', 'HORROR'),
    )

    image = models.ImageField(upload_to='books/',verbose_name='загрузите фото')
    title = models.CharField(max_length=100, verbose_name='укажите название книги') 
    description = models.TextField(verbose_name='укажите описание книги',blank=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену книги',default=200)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=10,choices=GENRE_CHOICES,verbose_name='выберите жанр книги')
    mail_author = models.CharField(max_length=100,verbose_name='укажите почту автора')
    author = models.CharField(max_length=100,default='Иван Иванов')
    link = models.URLField(verbose_name='укажите ссылку из youtube')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='книга'
        verbose_name_plural='книги'
    
class Review(models.Model):
    STARS = (
        ("🌟", "🌟"),
        ("🌟🌟", "🌟🌟"),
        ("🌟🌟🌟", "🌟🌟🌟"),
        ("🌟🌟🌟🌟", "🌟🌟🌟🌟"),
        ("🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟"),
    )
    choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='choice_book')
    created_at = models.DateField(auto_now=True)
    text_review = models.TextField(default='Хороший фильм')
    stars = models.CharField(max_length=10, choices=STARS,default='🌟🌟')
    
    def __str__(self):
        return f'{self.stars}-{self.choice_book.title}'

    
    
    
    
    
    
    
    
       