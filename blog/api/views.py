from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostListApiView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    queryset = Post.published.all()

class PostApiView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    queryset = Post.published.all()

class DestroyApiView(LoginRequiredMixin,generics.RetrieveDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    queryset = Post.published.all()

# class PostDetailApiView(generics.RetrieveAPIView):
#     lookup_field = 'pk'
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         pk=self.kwargs.get('pk')
#         return Post.published.get(pk=pk)
