
from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'book', api.BookViewSet)
router.register(r'category', api.CategoryViewSet)
router.register(r'user', api.UserViewSet)
router.register(r'bookcategory', api.BookCategoryViewSet)
router.register(r'userhistory', api.UserHistoryViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)
