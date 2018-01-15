from mongoengine import connect, Document, StringField


connect('crawler')


class Domain(Document):
    scheme = StringField(max_length=120, required=True)
    netloc = StringField(max_length=255, required=True)

    meta = {'allow_inheritance': True}
