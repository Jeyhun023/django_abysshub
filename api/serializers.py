from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product 
        fields = '__all__'

class ForumSearchSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField(source='_id')
    user = serializers.CharField(source='_source.user', required=False)
    title = serializers.CharField(source='_source.title', required=False)
    slug = serializers.SlugField(source='_source.slug', required=False)
    description = serializers.CharField(source='_source.description', required=False)
    tags = serializers.CharField(source='_source.tags', required=False)
    accepted_answer_id = serializers.IntegerField(source='_source.accepted_answer_id', required=False)
    answer_count = serializers.IntegerField(source='_source.answer_count', required=False)
    comment_count = serializers.IntegerField(source='_source.comment_count', required=False)
    view_count = serializers.IntegerField(source='_source.view_count', required=False)
    upvote = serializers.IntegerField(source='_source.upvote', required=False)
    downvote = serializers.IntegerField(source='_source.downvote', required=False)
    type = serializers.CharField(source='_source.type', required=False)
    product = serializers.CharField(source='_source.product', required=False)
    last_active_at = serializers.DateTimeField(source='_source.last_active_at', required=False)
    closed_at = serializers.DateTimeField(source='_source.closed_at', required=False)
    isEdited = serializers.BooleanField(source='_source.isEdited', required=False)
    created_at = serializers.DateTimeField(source='_source.created_at', required=False)
    updated_at = serializers.DateTimeField(source='_source.updated_at', required=False)

    