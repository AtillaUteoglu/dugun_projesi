from django.contrib import admin
from .models import Ani

# Sadece bu satır kalsın, üstteki @... satırını sil
admin.site.register(Ani)