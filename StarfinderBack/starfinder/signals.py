from django.db.models.signals import post_save, pre_save
from .models import AbilityValue

@receiver(post_save, sender=AbilityValue)
def ability_value_post_save(sender, instance, **kwargs):
    """Обработка сигнала изменения характеристики"""
    if not kwargs['created']:
        instance.character.on_change_ability_value(instance)