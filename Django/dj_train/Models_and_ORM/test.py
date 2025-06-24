from django.db.models import Count,Author

authors = Author.objects.annotate(book_count = Count('book'))
for author in authors:
    print(author.name, author.book)