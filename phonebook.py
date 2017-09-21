#Create a contact list
#create a class for contacts
#create a loop that prompts to add, delete and search contact


class ContactManger:

    def __init__(self, person={}):

        self.person = person

    def add_person(self):

        name = input("enter your name: ")
        phone_number = input("enter your phone_number: ")
        email_address = input("enter your email_address: ")
        postal_address = input("enter your postal_address: ")

        self.person.setdefault(name,[]).append(phone_number)
        self.person[name].append(email_address)
        self.person[name].append(postal_address)

        for name in self.person.keys():
            print(name)

    def search(self,find):

        if find in self.person.keys():
            look = self.person[find]
            print ("phone_no: " + look[0] + ' email: ' + look[1] + ' postal: ' + look[2])

    def remove(self,rmve):

        if rmve in self.person.keys():
            del self.person[rmve]
            print (" Contact deleted ")

    def show_contact(self):
        for show in self.person.keys():
            for details in self.person.values():
                print (show, " ".join(details))     #joins the values of a list into a joint string




new = ContactManger()

check = input("To add contact press 1, To search name press 2, To delete contact press 3, To show contact 4, To exit press 5:  " )

while check != "5":

    if check == "1":
        new.add_person()

    elif check == "2":
        new.search(input("Enter name : "))

    elif check == "3":
        new.remove(input("Enter name: "))

    elif check == "4":
        new.show_contact()


    check = input("To add contact press 1, To search name press 2, To delete contact press 3, To show contact 4, To exit press 5: ")

