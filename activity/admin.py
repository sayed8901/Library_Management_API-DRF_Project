from django.contrib import admin
from .models import Borrow

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('id', 'borrowed_by_user', 'borrowed_book', 'borrowed_date', 'borrow_for', 'return_deadline', 'is_returned')
    # list_filter = ('borrowed_date', 'return_deadline', 'is_returned')
    search_fields = ('borrowed_by_user__username', 'borrowed_book__title')
    list_editable = ('is_returned',)
    ordering = ('-borrowed_date',)
    date_hierarchy = 'borrowed_date'

    def get_queryset(self, request):
        # Annotate queryset if necessary or modify default behavior
        queryset = super().get_queryset(request)
        return queryset
