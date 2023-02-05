from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from core.models import *


@receiver(post_delete, sender=Participation)
def _handel_owner_delete(instance: Participation, **kwargs):
    if instance.permission is Participation.OWNER:
        try:
            instance.board.change_random_owner()
        except NoOtherUserException:
            instance.board.delete()


@receiver(post_save, sender=Board)
def _set_board_slug(instance: Board, **kwargs):
    instance.slug = instance.name + instance.pk
