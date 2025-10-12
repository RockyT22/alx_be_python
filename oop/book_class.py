class Book:
    def __init__(self, title, author, year):
        """
        Constructor: Initializes a Book instance.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor: Called when the instance is about to be destroyed.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation: Returns a user-friendly description.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Returns a string that can recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
