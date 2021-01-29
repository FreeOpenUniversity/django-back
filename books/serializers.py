
from rest_framework.compat import LONG_SEPARATORS
from .models import *

from rest_framework.serializers import ModelSerializer
class CategorySerializer(ModelSerializer):
  class Meta:
      model = Category
      fields = ('id','name',)

class BookSerializer(ModelSerializer):
  class Meta:
      model = Book
      fields = ('id','title','url','categories')
  
  categories = CategorySerializer(many=True)
  def create(self, validated_data):
        cat_ser = CategorySerializer(many=True).create
        categories_data = cat_ser(validated_data.pop('categories'))
        book:Book = Book.objects.create(**validated_data)
        book.categories.set(categories_data)
        return book

class UserSerializer(ModelSerializer):
  class Meta:
      model = User
      fields = ('id','name','email','password','intro')


class BookCategorySerializer(ModelSerializer):
  class Meta:
      model = BookCategory
      fields = ('id','book','category','user')


class UserHistorySerializer(ModelSerializer):
  class Meta:
      model = UserHistory
      fields = ('id','progress','book','user')