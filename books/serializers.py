
from .models import *

from rest_framework.serializers import ModelSerializer

class CategorySerializer(ModelSerializer):
  class Meta:
      model = Category
      fields = ('name',)

class BookSerializer(ModelSerializer):
  class Meta:
      model = Book
      fields = ('title','url','category')

class UserSerializer(ModelSerializer):
  class Meta:
      model = User
      fields = ('name','email','password_digest','intro')


class BookCategorySerializer(ModelSerializer):
  class Meta:
      model = BookCategory
      fields = ('book','category','user')


class UserHistorySerializer(ModelSerializer):
  class Meta:
      model = UserHistory
      fields = ('progress','book','user')