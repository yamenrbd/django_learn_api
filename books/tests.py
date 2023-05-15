from django.test import TestCase
from django.urls import reverse

from .models import Book

# Create your tests here.


# class for test with name of model and folowed with test ModelTest --> BookTest
# it have to be named like this other wise will not work
# note that all test must start with name test like (test_book_content, test_book_listview)
class BookTest(TestCase):
    @classmethod
    # create an object of model and fill the data
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title=" A good test title",
            subtitle=" A good test subtitle",
            author=" name of som author for test",
            isbn="some ISBN number for test",
        )

    # check the data on the model that have been created in setUpTestData
    def test_book_content(self):
        self.assertEqual(self.book.title, " A good test title")
        self.assertEqual(self.book.subtitle, " A good test subtitle")
        self.assertEqual(self.book.author, " name of som author for test")
        self.assertEqual(self.book.isbn, "some ISBN number for test")

    # check the HTML views and links
    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, " A good test subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")
