from django.test import TestCase
from django.urls import reverse


from .models import Author, Book


class AuthorDetailViewTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name='John',
            last_name='Doe',
            bio='Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        )
        self.book1 = Book.objects.create(
            title='Book 1',
            author=self.author,
            language='EN',
            pages=300
        )
        self.book2 = Book.objects.create(
            title='Book 2',
            author=self.author,
            language='EN',
            pages=250
        )
        self.url = reverse('author_detail', args=[self.author.pk])

    def test_author_detail_view_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_author_detail_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'author_detail.html')

    def test_author_detail_view_displays_author_info(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.author.first_name)
        self.assertContains(response, self.author.last_name)
        self.assertContains(response, self.author.bio)

    def test_author_detail_view_displays_books_by_author(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book2.title)