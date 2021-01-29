

from . import models
from . import serializers
from rest_framework import viewsets, permissions,status
from rest_framework.response import Response

class bulkModelViewset(viewsets.ModelViewSet):
    filterset_fields = "__all__"
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class BookViewSet(bulkModelViewset):
    """ViewSet for the Book class"""

    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    # permission_classes = [permissions.IsAuthenticated]
    

class CategoryViewSet(bulkModelViewset):
    """ViewSet for the Category class"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserViewSet(bulkModelViewset):
    """ViewSet for the User class"""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class BookCategoryViewSet(bulkModelViewset):
    """ViewSet for the BookCategory class"""

    queryset = models.BookCategory.objects.all()
    serializer_class = serializers.BookCategorySerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserHistoryViewSet(bulkModelViewset):
    """ViewSet for the UserHistory class"""

    queryset = models.UserHistory.objects.all()
    serializer_class = serializers.UserHistorySerializer
    # permission_classes = [permissions.IsAuthenticated]
