class Contact:
    phonebook=[]
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        Contact.phonebook.append(self)

    # @staticmethod  **We can not declare, as it can not accept the object instance as input.
    #it needs a positional argument
    def show_contact(self):
        return f"Person Name:{self.name},contact number:{self.phone}"

    @classmethod
    def show_all_contact(cls):
        if len(cls.phonebook)==0:
            print("No contacts available in phone book")
        else:
            for contact in cls.phonebook:
                # print(contact.phonebook)
                #print(f"Name:{contact.name},Phone:{contact.phone}")
                print(contact.show_contact())

c1=Contact('carol',445689523)
c2=Contact('jack',885894665)

# print(c1.phonebook)
# print(c2.phonebook)
c1.show_all_contact()
