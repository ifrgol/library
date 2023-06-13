from rest_framework.views import APIView

from authors.models import Author
from books.models import Book
from books.serializers import BookSerializer, BookSerializerV2
from authors.serializers import AuthorSerializer
from authors.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets


class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        book = self.get_object()
        return Response(book.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'books': reverse('book-list', request=request, format=format),
        'authors': reverse('author-list', request=request, format=format)
    })


class AddBook(APIView):
    def post(self, request, *args, **kwargs):
        book_serializer = BookSerializerV2(request['data'])
        book_serializer.is_valid(raise_exception=True)
        book_serializer.save()
        return self.create(request, *args, **kwargs)

    def get(self, request, format=None,):
        books = Book.objects.all()
        serializer = BookSerializerV2(books, many=True)
        return Response(serializer.data)

