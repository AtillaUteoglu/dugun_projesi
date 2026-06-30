from django.db import models

class Ani(models.Model):
    isim_soyisim = models.CharField(max_length=100)
    mesaj = models.TextField()
    # Kaliteyi korumak için ImageField kullanıyoruz
    dosya = models.ImageField(upload_to='anilar/') 
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.isim_soyisim