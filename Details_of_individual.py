class Member:
    def __init__(self,name):
        self.name=name
    def personaldetails(self,address,hometown,country,contact_no):
        self.address=address
        self.hometown=hometown
        self.country=country
        self.contact_no=contact_no
    def physicalDetails(self,height,weight,BMI):
        self.height=height
        self.weight=weight
        self.BMI=BMI
member1=Member(input("Enter the name of member: "))

class filling_details:
    def givingdetails(self):
        member1.address=input("Enter your address: ")
        member1.hometown = input("Enter your hometown: ")
        member1.country = input("Enter your country of residence: ")
        member1.contact_no = input("What is your contact number? ")
        member1.height = int(input("How much tall are you? "))
        heightInM = member1.height * 30.48
        member1.weight = int(input("What is your weight? "))
        weightinKg = member1.weight / 10
        print(member1.name + ", your details are;")
        print("My address is ",member1.address)
        print("My Hometown is ",member1.hometown)
        print("I am from ",member1.country)
        print("My contact number is ",member1.contact_no)
        print("I am "+str(heightInM)+ " cms tall.")
        print("My weight is "+str(member1.weight)+" N.")
        member1.BMI=print("My BMI is "+str(heightInM/weightinKg)+" .")
    member1=givingdetails(member1.name)


