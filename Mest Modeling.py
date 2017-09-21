class School():

    def __init__(self, eits= [], fellows = []):
        self.eits = eits
        self.fellows = fellows

    def mesters (self,eit):
        self.eits.append(eit)
        return print ("mester {} added to register".format(eit.names))


    def mest_fellows (self,staff):
        self.fellows.append(staff)
        return print("New staff {} hired".format(staff.name))

class Person():

    def __init__(self,name,nationality):
        self.name = name
        self.nationality = nationality


class Eit(Person):

    def __init__(self, name, nationality):
        super().__init__(name,nationality)
        # self.fun_fact = fun_facts



        #super() used for inheritance of functionality from other classes

        # self.names = input("EIt name: ")
        # self.nationalities = input("enter nationality: ")


        # print("My name is {} i am from {} and i love tech class because {}".format(self.names,self.nationalities,self.fun_fact))


class Fellow(Person):

    def __init__(self,name, nationality):
        super().__init__(name,nationality)

        # self.name = name
        # self.nationality = nationality
    # def add_name(self,name):
    #     self.name = name
    #     return self.name
    # def add_nationality(self,nationality):
    #     se
    #     return self.nationality

        # content = input("How happy are you on a scale of 1-10: ")
        # content = int(content)
        # if content <= 5:
        #     print("sad")
        # else:
        #     print("happy")

        # self.happiness_level = random
# class Person():

    # def __init__(self, name, nationality):




name = input("Enter name: ")
nationality = input("Enter Country: ")


mester = Eit(name,nationality)
fell = Fellow(name, nationality)
# mest = School()
print(fell.name,fell.nationality)
print(mester.name,mester.nationality)
