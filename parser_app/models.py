from django.db import models

class MashinaModel(models.Model):
    title = models.CharField(max_length=500)
    price = models.CharField(max_length=100)
    block_counter = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    
    def str(self):
        return self.title
    
class RezkaModel(models.Model):
    title = models.CharField(max_length=500)

    def str(self):
        return self.title