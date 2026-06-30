from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from dugun_app import views  # views dosyasını buradan çağırıyoruz


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ana sayfa (Galeri)
    path('', views.ana_sayfa_galeri, name='galeri'),
    
    # Yükleme sayfası
    path('yukle/', views.yukleme_sayfasi, name='yukle'),
    path('album/<str:isim>/', views.album_detay, name='album_detay'),
]

# Medya dosyaları için ayar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
