from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# =====================ПОЛЬЗОВАТЕЛИ==============================
USER_MODEL = settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    third_name = models.CharField(max_length=15, blank=True)
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

# =====================ЗАЯВКИ====================================
class Application(models.Model):
    STATUS_CHOICES = [
        ('new', 'НОВАЯ'),
        ('approved', 'ПОДТВЕРЖДЕНО'),
        ('rejected', 'ОТКЛОНЕНО'),
    ]
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    car = models.CharField(max_length=10)
    descr = models.TextField(max_length=300)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

    class Meta:
        verbose_name = "Заявление"
        verbose_name_plural = "Заявления"

    def __str__(self):
        return f"Application for {self.car} - {self.get_status_display()}"