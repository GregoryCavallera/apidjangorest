from quickstart.serializers import ArticleSerializer
from rest_framework import generics
from quickstart.models import Article

# Create your views here.

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer