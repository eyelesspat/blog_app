from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
def home(request):
    return render(request, 'blog/index.html')