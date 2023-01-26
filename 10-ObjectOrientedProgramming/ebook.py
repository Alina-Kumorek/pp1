class Book():

    def __init__(self, title, author, no_of_pages):
        self.title = title
        self.author = author
        self.no_of_pages = no_of_pages
        self.is_open = False
        self.page = 0

        self.pages = []
        for p in range(self.no_of_pages):
            if p == 0:
                self.pages.append(f"{self.title}\nby {self.author}")
            else:
                self.pages.append(f"This is the content of the page #{p+1}")
    
    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
    
    def page_inc(self):
        if self.is_open:
            if self.page < self.no_of_pages - 1:
                self.page += 1
    
    def page_dec(self):
        if self.is_open:
            if self.page > 0:
                self.page -= 1
    
    def read(self):
        if self.is_open:
            print(self.pages[self.page])
            self.page_inc()
        else:
            print("The book is closed.")
    
    def status(self):
        # Display a book status (title, author, page numbers, current page no)
        print(f"Title:\t{self.title}\nAuthor:\t{self.author}\nPages:\t{self.no_of_pages}\nCurrent page #:\t{self.page + 1}")
        if self.is_open:
            print("The book is open.")
        else:
            print("The book is closed.")