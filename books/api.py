

from . import models
from . import serializers
from rest_framework import viewsets, permissions,status
from rest_framework.response import Response


def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
    serializer.is_valid(raise_exception=True)

    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class BookViewSet(viewsets.ModelViewSet):
    """ViewSet for the Book class"""

    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    create = create
    filterset_fields = "__all__"

class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Category class"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for the User class"""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the BookCategory class"""

    queryset = models.BookCategory.objects.all()
    serializer_class = serializers.BookCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class UserHistoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the UserHistory class"""

    queryset = models.UserHistory.objects.all()
    serializer_class = serializers.UserHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
