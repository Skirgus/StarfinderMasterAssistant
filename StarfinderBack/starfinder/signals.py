from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AbilityValue, Character

@receiver(post_save, sender=AbilityValue)
def ability_value_post_save(sender, **kwargs):
    """Обработка сигнала изменения характеристики"""
    if not **kwargs['created']:
        sender.character.on_change_ability_value(sender)