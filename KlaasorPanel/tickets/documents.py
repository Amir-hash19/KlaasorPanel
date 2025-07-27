from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Ticket, TicketMessage



ticket_index = Index('tickets')


@registry.register_document
class TicketDocument(Document):
    user = fields.ObjectField(properties={
        "username": fields.TextField(),
        "email":fields.TextField(),
    })

    bootcamp = fields.ObjectField(properties={
        "name": fields.TextField(),

    })

    class Index:
        name = 'tickets'



    class Django:
        model = Ticket
        fields = [
            'subject',
            'category',
            'status',
            'created_at',
            'updated_at'
        ]    
