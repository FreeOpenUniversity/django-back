
from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'books', api.BookViewSet)
router.register(r'categories', api.CategoryViewSet)
router.register(r'users', api.UserViewSet)
router.register(r'book_categories', api.BookCategoryViewSet)
router.register(r'user_histories', api.UserHistoryViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('api/', include(router.urls)),
    path("api/search", views.search, name="search")
)
