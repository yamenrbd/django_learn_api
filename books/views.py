from django.shortcuts import render
from .models import Book
from django.views.generic import ListView

# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    # default name of returning object will be modelname_list like book_list
