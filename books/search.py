from elasticsearch_dsl import Document, Text, Date, Search, connections
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

# use for redis
# connections.create_connection(hosts=['elasticsearch:9200'], timeout=20)


# use for local
connections.create_connection(hosts=['localhost'], timeout=20)


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


# search function using ElasticSearch: search all fields in DB exclude "created_at" field
def search(content):
    s = Search().query("multi_match", query=content,
                       fields=[
                           'title',
                           'content',
                           'user'])
    response = s.execute()
    return response
