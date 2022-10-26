from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response


# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass
    
class ArticleDetailView(APIView):
    def get(self, request, article_id):
        pass
    def put(self, request, article_id):
        pass
    def delete(self, request, article_id):
        pass
