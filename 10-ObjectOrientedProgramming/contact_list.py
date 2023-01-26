
class Contact_List():

    def __init__(self):
        self.list = []
    
    def add(self, contact):
        self.list.append(contact)
    
    def display(self):
        for i in self.list:
            print(i.name.ljust(20), i.email.ljust(24), i.tel)