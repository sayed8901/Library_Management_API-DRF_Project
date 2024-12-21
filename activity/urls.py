from django.urls import path, include
from .views import BorrowBookView, BorrowedBooksView, ReturnBookView


urlpatterns = [
    path('borrow/<int:pk>/', BorrowBookView.as_view(), name='borrow-book'),
    path('borrowed_books/', BorrowedBooksView.as_view(), name='borrowed-books-list'),

    path('return/<int:pk>/', ReturnBookView.as_view(), name='return-book'),
]

