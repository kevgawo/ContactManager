#mest is throwing a networking party. Write a software that registers guests.
#Take user input to store names and corresponding emails in  a dictionary
#Given a name , output and email
#Send an email to all guests thanking them for coming
#If the guest has an odd number of letters in the name send them a different email telling them they are unwelcomed to future events.




guestlist={}

while True:

    choose = input("press 1 to register and 2 to search: ")

    if choose == "1":

        name = input("enter name:")
        email = input("enter email: ")
        guestlist[name] = email

    elif choose == "2":

        name_found = input("enter name: ")

        if name_found in guestlist.keys():
            print(" the email address is ",email)


    else:
        break


#unpack the vthe dictionary and assign keys and valuews to the arguments you provide

for name,email in guestlist.items():
    print("the guest name is {} and their email {}.".format(name, email))

# print(guestlist)
# print("press 1 to exit")


