from elasticsearch_dsl import Document, Text, Date
from elasticsearch_dsl.connections import connections

# Establish connection to Elasticsearch
connections.create_connection(hosts=['localhost'])

class TodoIndex(Document):
    title = Text(analyzer='standard')
    description = Text(analyzer='standard')
    created_at = Date()
    updated_at = Date()

    class Index:
        name = 'todos'  # Index name in Elasticsearch

    def save(self, **kwargs):
        return super().save(**kwargs)
