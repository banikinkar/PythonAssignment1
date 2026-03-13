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

    @classmethod
    def search_contact(cls,search_name):
        for contact in cls.phonebook:
            if contact.name.lower()==search_name.lower():
                return contact.phone
        return f"No contact found in the phone book for {search_name}"

    @staticmethod
    def validate_contact(number):
        if len(number)==0 or len(number)!=10 or number.isdigit():
            return f"Invalid phone number {number}"
        else:
            return True

n_contact=int(input("how many contacts do you want to search :"))
for i in range(n_contact):
    name=input("enter the name of the contact :")
    phone=input("enter the contact phone :")
    if Contact.validate_contact(phone):
        Contact(name,phone)
    else:
        print(f"Invalid phone number {phone}")

# c1=Contact('carol',445689523)
# c2=Contact('jack',885894665)

# print(c1.phonebook)
# print(c2.phonebook)
# c1.search_contact('jack')

Contact.show_all_contact()
