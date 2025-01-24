from elasticsearch_dsl import Document, Text, Date, analyzer
from elasticsearch_dsl.connections import connections

# Establish connection to Elasticsearch
connections.create_connection(hosts=["http://localhost:9200"])

ngram_analyzer = analyzer(
    "ngram_analyzer", tokenizer="ngram", filter=["lowercase"], char_filter=[]
)

phonetic_analyzer = analyzer(
    "phonetic_analyzer", tokenizer="standard", filter=["lowercase", "phonetic"]
)


class TodoIndex(Document):
    title = Text(analyzer="standard")
    # title = Text(analyzer=ngram_analyzer)
    description = Text(analyzer="standard")
    created_at = Date()
    updated_at = Date()

    class Index:
        name = "todos"  # Index name in Elasticsearch

    def save(self, **kwargs):
        return super().save(**kwargs)
