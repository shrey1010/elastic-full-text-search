from django.core.management.base import BaseCommand
from todo.models import Todo
from todo.search_indexes import TodoIndex


class Command(BaseCommand):
    help = "Sync Todos to Elasticsearch"

    def handle(self, *args, **kwargs):
        # Clear existing index
        TodoIndex.init()

        # Sync all Todos to Elasticsearch
        for todo in Todo.objects.all():
            doc = TodoIndex(
                meta={"id": todo.id},
                title=todo.title,
                description=todo.description,
                created_at=todo.created_at,
                updated_at=todo.updated_at,
            )
            doc.save()

        self.stdout.write(self.style.SUCCESS("Todos synced to Elasticsearch!"))
