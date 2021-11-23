from django.shortcuts import render
from rest_framework import generics, permissions

from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly
from posts.serializers import PostSerializer
# Create your views here.


class Post_list(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class Post_detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer