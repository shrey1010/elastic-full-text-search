from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from todo.models import Todo
from todo.search_indexes import TodoIndex

@receiver(post_save, sender=Todo)
def sync_todo_to_elasticsearch(sender, instance, **kwargs):
    doc = TodoIndex(
        meta={'id': instance.id},
        title=instance.title,
        description=instance.description,
        created_at=instance.created_at,
        updated_at=instance.updated_at
    )
    doc.save()

@receiver(post_delete, sender=Todo)
def delete_todo_from_elasticsearch(sender, instance, **kwargs):
    TodoIndex(meta={'id': instance.id}).delete()
