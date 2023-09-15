from rest_framework import serializers
from .models import AuthorModel,BookModel

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('__all__')


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('__all__')

