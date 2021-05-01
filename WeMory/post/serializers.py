from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('created_at' , 'updated_at', 'author', 'diary', 'received_money',
                'image', 'title', 'content')


 