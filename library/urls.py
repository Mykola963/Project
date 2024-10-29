from django.urls import path
from .views import AuthorListView, AuthorDetailView, BookListView, BookDetailView, index
from . import views

app_label = 'library'

urlpatterns = [
    path('', index, name='index'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.authors_list, name='authors_list'),
    path('books/', views.books_list, name='books_list'),
]
