from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Task

@receiver(post_save, sender=Task)
def log_task_save(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    print(f'Task {instance.title} was {action}.')

@receiver(post_delete, sender=Task)
def log_task_delete(sender, instance, **kwargs):
    print(f'Task {instance.title} was deleted.')
