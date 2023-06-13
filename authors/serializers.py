from rest_framework import serializers
from authors.models import Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='author-highlight', format='html')

    class Meta:

        model = Author
        fields = ['url', 'id', 'highlight', 'owner', 'name', 'password', 'email']

    def create(self, validated_data):

        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


