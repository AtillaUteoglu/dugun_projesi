from django.shortcuts import render, redirect
from .models import Ani
from .forms import AniForm
from itertools import groupby
from collections import defaultdict
from itertools import groupby

def galeri_goruntule(request):
    # Verileri 'isim_soyisim'e göre sıralayarak çekiyoruz (Gruplama için şart)
    anilar = Ani.objects.all().order_by('isim_soyisim', '-id')
    return render(request, 'galeri.html', {'anilar': anilar})
        
    return render(request, 'galeri.html', {'gruplu_veriler': dict(gruplu_sozluk)})

def album_detay(request, isim):
    # Sadece o isme ait fotoğrafları çek
    anilar = Ani.objects.filter(isim_soyisim=isim).order_by('-id')
    return render(request, 'album_detay.html', {'anilar': anilar, 'isim': isim})

def ana_sayfa_galeri(request):
    anilar = Ani.objects.all().order_by('-id')
    return render(request, 'galeri.html', {'anilar': anilar})

def yukleme_sayfasi(request):
    if request.method == 'POST':
        # form = AniForm(request.POST, request.FILES)  <-- Bunu kaldır veya yorum satırı yap
        
        # Dosyaları al
        files = request.FILES.getlist('dosya')
        isim = request.POST.get('isim_soyisim')
        mesaj = request.POST.get('mesaj')
        
        # Her biri için veritabanına kayıt at
        for f in files:
            Ani.objects.create(
                dosya=f,
                isim_soyisim=isim,
                mesaj=mesaj
            )
        return redirect('galeri') # Kendi URL ismini yaz
        
    else:
        form = AniForm()
        
    return render(request, 'yukle.html', {'form': form})

def ani_ekle(request):
    if request.method == 'POST':
        # HTML'den gelen dosyaları liste olarak yakala
        files = request.FILES.getlist('dosya')
        isim = request.POST.get('isim_soyisim')
        mesaj = request.POST.get('mesaj')
        
        # Her bir fotoğrafı ayrı bir kayıt olarak oluştur
        for f in files:
            Ani.objects.create(
                dosya=f,
                isim_soyisim=isim,
                mesaj=mesaj
            )
            
        return redirect('galeri_sayfasi') # URL isminiz neyse onu yazın
    
    return render(request, 'ani_ekle.html')