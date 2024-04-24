from elasticsearch_dsl import Document, Text, Keyword
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Passport

@registry.register_document
class PassportDocument(Document):
    class Index:
        name = 'passports'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Passport
        fields = [
            'name',
            'report_title',
            # Добавьте другие поля по мере необходимости
        ]