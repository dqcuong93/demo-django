from elasticsearch_dsl import Document, Text, Date, Search, connections
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models
from kafka import KafkaConsumer

# use for Docker ElasticSearch
# connections.create_connection(hosts=['elasticsearch:9200'], timeout=20)


# use for local ElasticSearch
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


# def search(content):
# """
# search function using ElasticSearch: search all fields in DB exclude "created_at" field
# """
#     s = Search().query("multi_match", query=content,
#                        fields=[
#                            'title',
#                            'content',
#                            'user'])
#     response = s.execute()
#     return response


def search():
    """
    search function using ElasticSearch: search all fields in DB exclude "created_at" field
    this function communicated through Kafka
    """

    # To consume latest messages and auto-commit offsets
    content = ''
    consumer = KafkaConsumer('store',
                             group_id='store-group',

                             # local machine setup
                             bootstrap_servers=['localhost:9092'],

                             # Docker setup
                             # bootstrap_servers=['kafka:9092'],

                             consumer_timeout_ms=1000)
    for message in consumer:
        content = message.value.decode('utf-8')
    consumer.close()
    s = Search().query("multi_match", query=content,
                       fields=[
                           'title',
                           'content',
                           'user'
                       ])
    response = s.execute()
    return response
