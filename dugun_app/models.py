from django.db import models
from cloudinary.models import CloudinaryField  # 1. Bunu ekle

class Ani(models.Model):
    isim_soyisim = models.CharField(max_length=100)
    mesaj = models.TextField()
    
    # 2. ImageField yerine bunu kullan:
    dosya = CloudinaryField('image') 
    
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.isim_soyisim