from mongoengine import connect, Document, StringField, DateTimeField, EmbeddedDocument, ListField, EmbeddedDocumentField
import datetime


connect(db='crawler')


class Url(EmbeddedDocument):
    path = StringField(max_length=255)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField()


class Domain(Document):
    scheme = StringField(max_length=120, required=True)
    netloc = StringField(max_length=255, required=True, unique=True)
    urls = ListField(EmbeddedDocumentField(Url))
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField()

    meta = {'allow_inheritance': True}
