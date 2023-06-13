from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:

        model = Book
        fields = ['url', 'id', 'owner', 'name', 'author_name', 'pages', 'publication_date', 'genre']

    def create(self, validated_data):

        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance


class BookSerializerV2(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
