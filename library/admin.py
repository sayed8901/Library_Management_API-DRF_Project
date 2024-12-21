from django.contrib import admin
from .models import Category, Book

# Register Category model with admin interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)


# Register Book model with admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'quantity')
    list_filter = ('category',)
    search_fields = ('title', 'author', 'category__name')

admin.site.register(Book, BookAdmin)
