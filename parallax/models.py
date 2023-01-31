from django.db import models


class Parallax(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    photo = models.ImageField(upload_to='photos', verbose_name="Фото", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фон"
        verbose_name_plural = "Фоны"
