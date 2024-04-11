from django.db import models



class Mahsulot(models.Model):
    nomi = models.CharField(max_length=150)
    soni = models.IntegerField()
    narxi = models.IntegerField()
    muddat = models.DateField()
    firma = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='phone/', blank=True)

    def __str__(self):
        return self.nomi