from rest_framework import status, viewsets, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from content_app.api import serializers
from content_app.models import Content, StreamPlatform, Review


class ContentListAV(APIView):

    def get(self, request):
        contents = Content.objects.all()
        serializer = serializers.ContentSerializer(contents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ContentDetailAV(APIView):

    def get(self, request, pk):
        try:
            content = Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ContentSerializer(content)
        return Response(serializer.data)

    def put(self, request, pk):
        content = Content.objects.get(pk=pk)
        serializer = serializers.ContentSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        content = Content.objects.get(pk=pk)
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = serializers.StreamPlatformSerializer


class ReviewList(generics.ListAPIView):
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(content=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class ReviewCreate(generics.CreateAPIView):
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        content = Content.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(
            content=content, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")

        if content.number_rating == 0:
            content.avg_rating = serializer.validated_data['rating']
        else:
            content.avg_rating = (
                content.avg_rating + serializer.validated_data['rating'])/2

        content.number_rating = content.number_rating + 1
        content.save()

        serializer.save(content=content, review_user=review_user)


class UserReview(generics.ListAPIView):
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return Review.objects.filter(review_user__username=username)
