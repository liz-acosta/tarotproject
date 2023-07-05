from django.db import models


class TarotCard(models.Model):
    symbol = models.CharField(max_length=200)
    number = models.CharField(max_length=2)
    meaning = models.TextField(blank=True)
    arcana = models.BooleanField(default=False)
    image_filename = models.CharField(max_length=200)

    # def __str__(self):
    #     return self