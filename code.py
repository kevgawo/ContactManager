class ContactManger:

    def __init__(self, name, phone_number, email_address, postal_address):

     self.name = name
     self.phone_number = phone_number
     self.email_address = email_address
     self.postal_address = postal_address



    def new_person(self):

        print(" ")
        print ("{}".format(self.name), "{}".format(self.phone_number),"{}".format(self.email_address),"{}".format(self.postal_address))



name = input("enter your name: ")
phone_number = input("enter your phone_number: ")
email_address = input("enter your email_address: ")
postal_address = input("enter your postal_address: ")

new = ContactManger(name, phone_number, email_address, postal_address)
print(new.new_person())

