from django.db import models
from users.models import User

class QRCode(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='qrcodes/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'qr_codes'
        verbose_name = 'QR Code'
        verbose_name_plural = 'QR Codes'