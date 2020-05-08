from elasticsearch_dsl import Document, Text, Date, Search, connections
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class BookIndex(Document):
    title = Text()
    content = Text()
    created_at = Date()
    user = Text()

    class Index:
        name = 'book-index'


def bulk_indexing():
    BookIndex.init()
    es = Elasticsearch()
    bulk(
        client=es,
        actions=(
            b.indexing() for b in models.Book.objects.all().iterator()
        )
    )


def search(user):
    s = Search().filter('term', user=user)
    response = s.execute()
    return response
