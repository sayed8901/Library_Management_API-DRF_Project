from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Book, Category
from .serializers import CategorySerializer, BookSerializer, BookListSerializer
from accounts.permissions import IsAdmin, IsMember, IsAdminOrReadOnly



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]


class AvailableBooksView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        books = Book.objects.filter(quantity__gt=0)
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
