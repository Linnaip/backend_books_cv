from rest_framework import viewsets
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
from .pagination import CustomPagination


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_fields = ('title',)
    pagination_class = CustomPagination


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_fields = ('username', 'last_name',)
    pagination_class = CustomPagination
