

from django.contrib import admin
from django import forms
from .models import Book, Category, User, BookCategory, UserHistory

class BookAdminForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'

class CategoryAdminForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'

class UserAdminForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'

class BookCategoryAdminForm(forms.ModelForm):
    
    class Meta:
        model = BookCategory
        fields = '__all__'

class UserHistoryAdminForm(forms.ModelForm):
    
    class Meta:
        model = UserHistory
        fields = '__all__'


class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    list_display = ['title', 'url', 'author']
    readonly_fields = []

admin.site.register(Book, BookAdmin)

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ['name']
    readonly_fields = []

admin.site.register(Category, CategoryAdmin)

class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ['name', 'email', 'password_digest', 'intro']
    readonly_fields = []

admin.site.register(User, UserAdmin)

class BookCategoryAdmin(admin.ModelAdmin):
    form = BookCategoryAdminForm
    list_display = ['book', 'category', 'user']
    readonly_fields = []

admin.site.register(BookCategory, BookCategoryAdmin)

class UserHistoryAdmin(admin.ModelAdmin):
    form = UserHistoryAdminForm
    list_display = ['progress', 'book', 'user']
    readonly_fields = []

admin.site.register(UserHistory, UserHistoryAdmin)

