# https://www.django-rest-framework.org/api-guide/viewsets/

from books.semanticSearch import handleQuestion
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.http import HttpResponse

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

class UserHistoryViewSet(viewsets.ModelViewSet):
    queryset = UserHistory.objects.all()
    serializer_class = UserHistorySerializer

def search(request):
    question  = request.GET["question"]
    return HttpResponse(handleQuestion(question), content_type="application/json")