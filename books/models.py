
from django.db.models import *
from django.db.models.deletion import CASCADE

class Book(Model):
  title=CharField(max_length=128)
  url=URLField()
  author=CharField(max_length=128)
  categories=ManyToManyField('Category', through='BookCategory', related_name="books")

class Category(Model):
  name=CharField(max_length=128)

class User(Model):
  name=CharField(max_length=128)
  email=EmailField()
  password_digest=CharField(max_length=128)
  intro=TextField()

class BookCategory(Model):
  book=ForeignKey(Book, on_delete=CASCADE)
  category=ForeignKey(Category, on_delete=CASCADE)
  # user=ForeignKey(User, on_delete=CASCADE)

class UserHistory(Model):
  progress=IntegerField()
  book=ForeignKey(Book, on_delete=CASCADE)
  user=ForeignKey(User, on_delete=CASCADE)

