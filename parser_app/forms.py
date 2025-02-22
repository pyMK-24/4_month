from django import forms
from . import models,parser_mashina,parser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('mashina.kg', 'mashina.kg'),
        ('rezka.ag','rezka.ag')
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    
    class Meta:
        fields = [
            'media_type',
        ]
    
    def parser_data(self):
        if self.data['media_type'] == 'mashina.kg':
            mashins = parser_mashina.parsing_mashina()
            for i in mashins:
                models.MashinaModel.objects.create(**i)
        elif self.data['media_type'] == 'rezka.ag':
            rezka_films = parser_rezka.parsing_rezka()
            for i in rezka_films:
                models.RezkaModel.objects.create(**i)