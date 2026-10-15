class Notebook:
    def __init__(self, notes_list):
        self.notes = notes_list  

    def show_notes(self):
        for index, note in enumerate(self.notes, start=1):
            print(f"{index}.{note}")  
my_notebook = Notebook(["Buy a book", "Read the book"]) 
my_notebook.show_notes() 
