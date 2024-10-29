from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Book


def index(request):
    return render(request, 'index.html', context={'books': Book.objects.all()})

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author=self.object)
        return context


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})
