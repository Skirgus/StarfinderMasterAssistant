from django.db import models

# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=255) # название расы
    min_average_weight = models.DecimalField(max_digits=5, decimal_places=2) # средний вес, нижняя граница
    max_average_weight = models.DecimalField(max_digits=5, decimal_places=2) # средний вес, верхняя граница
    min_average_height = models.DecimalField(max_digits=5, decimal_places=2) # средний рост, нижняя граница
    max_average_height = models.DecimalField(max_digits=5, decimal_places=2) # средний рост, нижняя граница
    age_of_majority = models.IntegerField() # возраст совершеннолетия
    basic_info = models.TextField() # базовая информация
    title_info = models.TextField() # информация для списка
    basic_image = models.ImageField(upload_to='races/', null=True, blank=True) # изображение
    title_image = models.ImageField(upload_to='races/', null=True, blank=True) # миниатюра для списка
    
    def __str__(self):
        return self.name


class RaceDescription(models.Model):
    title = models.CharField(max_length=255) # заголовок
    text = models.TextField() # описание
    race = models.ForeignKey('Race',  related_name='descriptions', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + '(' + self.race.name + ')'


class RacePlayingFor(models.Model):
    YOUR_MOST_LIKELY = 'YOUR'
    OTHER_RACES_MOST_LIKELY = 'OTHER'
    PLAYING_FOR_CHOICES = (
        (YOUR_MOST_LIKELY, 'Вы скорее всего...'),
        (OTHER_RACES_MOST_LIKELY, 'Другие расы скорее всего...')
    )
    title = models.CharField(max_length=255,choices=PLAYING_FOR_CHOICES, default=YOUR_MOST_LIKELY) # заголовок
    text = models.TextField() # описание
    race = models.ForeignKey('Race',  related_name='playingforinformations', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text + '(' + self.race.name + ')'