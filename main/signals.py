from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Student


@receiver(post_save, sender=Student)
def post_save_user(**k):
    print(f'Ученик создан')

