class Book(object):
    def __init__(self, title, author, pages):
        print('A book is created.')
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'Title.%s, author.%s, pages.%s.' %(self.title, self.author, self.pages)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('A book is destroyed.')

book1 = Book('Curso de Python', 'Rodrigo', 150)

print(book1)
print(len(book1))
del(book1)