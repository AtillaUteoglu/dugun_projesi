from django import forms
from .models import Ani

class AniForm(forms.ModelForm):
    class Meta:
        model = Ani
        fields = ['isim_soyisim', 'mesaj', 'dosya']
        # İstersen burada etiketleri (label) de Türkçe yapabilirsin:
        labels = {
            'isim_soyisim': 'Adınız Soyadınız',
            'mesaj': 'Paylaşmak istediğiniz mesaj',
            'dosya': 'Fotoğrafınız'
        }