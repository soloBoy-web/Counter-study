from django.db import models
from django.conf import settings


class Counter(models.Model):
    value = models.IntegerField(default=0)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  # сделал каскад гарантирует что у пользователя только один счетчик
        primary_key=False,  # теперь каждому счетчику обязательно должен соответствовать пользователь
        related_name = 'counter' # обратная связь ?
    )

    def __str__(self):
        return f"id={self.id} value={self.value}"
