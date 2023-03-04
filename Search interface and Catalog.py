# Search interface and Catalog:
# The Catalog class will implement the Search interface to facilitate searching of books.


from abc import ABC


def search_by_subject(subject):
    None


def search_by_pub_date(publish_date):
    None


class Search(ABC):
    def search_by_title(self, title):
        None

    def search_by_author(self, author):
        None


class Catalog(Search):
    def __init__(self):
        self.__book_titles = {}
        self.__book_authors = {}
        self.__book_subjects = {}
        self.__book_publication_dates = {}

    def search_by_title(self, query):
        # return all books containing the string query in their title.
        return self.__book_titles.get(query)

    def search_by_author(self, query):
        # return all books containing the string query in their author's name.
        return self.__book_authors.get(query)
