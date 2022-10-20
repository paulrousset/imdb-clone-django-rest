from rest_framework import serializers

from content_app.models import Content, Review, StreamPlatform


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ("content",)
        # fields = "__all__"


class ContentSerializer(serializers.ModelSerializer):
    platform = serializers.CharField(source="platform.name")

    class Meta:
        model = Content
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
