from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()


    def __str__(self):
        return self.name