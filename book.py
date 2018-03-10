# Developer: Nathan Kurz
# Course: CS 4308 (Concepts of Programming Languages)
# Instructor: Betty Kretlow

class Book(object):
    """ A standard book with the following attributes:

        - Author
        - Title
        - Number of Pages
    """

    def __init__(self, title, author, numPages):
        self.title = title
        self.author = author
        self.numPages = numPages

    # Setter for changing the title
    def setTitle(self, title):
        self.title = title

    # Getter for title
    def getTitle(self):
        return self.title

    # Outputs the title to console
    def printTitle(self):
        print(self.title)

    # Setter for author
    def setAuthor(self, author):
        self.author = author

    # Getter for author
    def getAuthor(self):
        return self.author

    # Outputs author to console
    def printAuthor(self):
        print(self.author)

    # Setter for number of pages
    def setNumPages(self, numPages):
        self.numPages = numPages

    # Getter for number of pages
    def getNumPages(self):
        return self.numPages

    # Output number of pages to console
    def printNumPages(self):
        print(self.numPages)

    def printAttributes(self):
        print('Author: ' + self.getAuthor())
        print('Title: ' + self.getTitle())
        print('Number of Pages: ' + self.getNumPages())
        print('\n')

# Request Input from user
print('\nEnter the title: ')
bookTitle = input()


print('\nEnter the author: ')
bookAuthor = input()


print('\nEnter number of pages: ')
bookNumPages = input()


# Create book object/instance
book1 = Book(bookTitle, bookAuthor, bookNumPages)

print('\n')

# Print book attributes
book1.printAttributes()

# Request a title change from user
print('Change the title of the book')

# Change title
book1.setTitle(input())
print('\n')

# Print altered attributes
book1.printAttributes()






    

