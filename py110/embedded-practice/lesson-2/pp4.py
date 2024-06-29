"""
How would you sort the following list of dictionaries based on the year
of publication of each book, from the earliest to the most recent?
"""

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

# expected:
# Pretty printed for clarity
[
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800'
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869'
    },
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967'
    }
]

def old_book_ranker(book):
    return int(book['published'])

sort_my_books = sorted(books, key=old_book_ranker)

print(sort_my_books)
# ! TODO review dictionary sorting here
