
from django import forms
from .models import *



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'url', 'author', 'category'],
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name'],
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password_digest', 'intro'],
class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = ['book', 'category', 'user'],
class UserHistoryForm(forms.ModelForm):
    class Meta:
        model = UserHistory
        fields = ['progress', 'book', 'user']
