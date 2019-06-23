from django.db import models

# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=255)
    min_average_weight = models.DecimalField(max_digits=5, decimal_places=2)
    max_average_weight = models.DecimalField(max_digits=5, decimal_places=2)
    min_average_height = models.DecimalField(max_digits=5, decimal_places=2)
    max_average_height = models.DecimalField(max_digits=5, decimal_places=2)
    age_of_majority = models.IntegerField()
    basic_info = models.TextField()
    title_info = models.TextField()
    basic_image = models.ImageField(upload_to='races/', null=True, blank=True)
    title_image = models.ImageField(upload_to='races/', null=True, blank=True)
    
    def __str__(self):
        return self.name


class RaceDescription(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
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
    title = models.CharField(max_length=255,choices=PLAYING_FOR_CHOICES, default=YOUR_MOST_LIKELY)
    text = models.TextField()
    race = models.ForeignKey('Race',  related_name='playingforinformations', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text + '(' + self.race.name + ')'