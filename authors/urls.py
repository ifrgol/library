from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet, basename="author")
router.register(r'books', views.BookViewSet, basename="book")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
