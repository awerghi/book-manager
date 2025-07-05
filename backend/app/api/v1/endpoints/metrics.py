from prometheus_client import Counter

BOOKS_CREATED   = Counter("books_created_total","Total books created")
BOOKS_WITH_NO_AUTHOR = Counter("searched_books_without_author","Total searched books without an author")
NOT_FOUND_BOOK_SEARCH = Counter("books_not_found","Books searched and not found")
