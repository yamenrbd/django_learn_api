from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from books.models import Book

# Create your tests here.


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title=" A good test title",
            subtitle=" A good test subtitle",
            author=" name of som author for test",
            isbn="some ISBN number for test",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)  # type: ignore
