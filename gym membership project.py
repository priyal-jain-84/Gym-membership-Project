import re
import time

cust_info={} #dict in the form of {phoneno: name, age, gender,Email, BMI, Membership Duration}
cust_regimen={} #dict of regimen in the form of {phoneno: Regimen}

class GYM:      
               

    def admin_menu(self):
        print ( '\nYou have entered the administrative section.\n' )
        print ( '1. Create a Member' )
        print ( '2. View Member' )
        print ( '3. Delete a member' )
        print ( '4. Update a member' )
        print ( '5. Create Regimen' )
        print ( '6. View Regimen' )
        print ( '7. Delete Regimen' )
        print ( '8. Update Regimen' )
        print ( '0. Exit' )

        time.sleep(1)

        try:
            self.call = int(input ( 'Enter the menu you want to visit: \n' ))
        
            
            if self.call == 1 :
                self.createMember ( )
            elif self.call == 2 :
                self.viewMember ( )
            elif self.call == 3 :
                self.delMember ( )
            elif self.call == 4 :
                self.updateMember ( )
            elif self.call == 5 :
                self.regCreate ( )
            elif self.call == 6 :
                self.regView ( )
            elif self.call == 7 :
                self.regDel ( )
            elif self.call == 8 :
                self.regUpdate ( )
            elif self.call == 0 :
                print ( '\nLogging out as admin...' )
                pass
            else :
                print ( 'Invalid Menu.\nPlease try again.' )
                self.admin_menu ( )


        except ValueError:
            print("Please select appropriate no...")
            self.admin_menu()




    def member_menu(self):
        print("Welcome to the Member Section...\n")
        print("1. Check profile..\n2. Check Regimen..\n0. Exit")

        try:
            
            self.call=int(input("Enter the menu you want to visit..\n"))

            if self.call==1:
                self.mem_profile()

            elif self.call==2:
                self.mem_regimen()

            elif self.call==0:
                print("\nLogging out as a member...")

            else:
                print("Invalid Menu.\nPlease try again.")
                self.member_menu()


        
        except ValueError:
            print("Please select appropriate no...")
            self.member_menu()
                  
            
            

    def Regimen(self,bmi,phoneno):
        self.phoneno=phoneno
        self.bmi=bmi

        if self.bmi<18.5:
            cust_regimen[self.phoneno]={
                'Mon' : 'Chest' ,
                'Tue' : 'Biceps' ,
                'Wed' : 'Rest' ,
                'Thu' : 'Back' ,
                'Fri' : 'Triceps' ,
                'Sat' : 'Rest' ,
                'Sun' : 'Rest'
            }

        elif self.bmi >= 18.5 and self.bmi < 25 :
            cust_regimen[self.phoneno] = {
                'Mon' : 'Chest' ,
                'Tue' : 'Biceps' ,
                'Wed' : 'Cardio/Abs' ,
                'Thu' : 'Back' ,
                'Fri' : 'Triceps' ,
                'Sat' : 'Legs' ,
                'Sun' : 'Rest'
            }

        elif self.bmi >= 25 and self.bmi < 30 :
            cust_regimen[self.phoneno] = {
                'Mon' : 'Chest' ,
                'Tue' : 'Biceps' ,
                'Wed' : 'Cardio/Abs' ,
                'Thu' : 'Back' ,
                'Fri' : 'Triceps' ,
                'Sat' : 'Legs' ,
                'Sun' : 'Cardio'
            }
            

        elif self.bmi >= 30 :
            cust_regimen[self.phoneno] = {
                'Mon' : 'Chest' ,
                'Tue' : 'Biceps' ,
                'Wed' : 'Cardio' ,
                'Thu' : 'Back' ,
                'Fri' : 'Triceps' ,
                'Sat' : 'Cardio' ,
                'Sun' : 'Cardio'
            }


    def createMember(self):
        print("\nCreate a member here...\n ")
        self.phone_no=int(input("Enter phone no here..."))
        self.name=input("Enter your name...")
        self.age=input("Enter your age...")
        self.gender=input("Enter 'M' for male, 'F' for female,'O' for other...")
        self.email=input("Enter your email id ...")
        self.BMI=int(input("Enter Body Mass Index..."))
        self.membershipDuration=int(input("Enter Duration of membership in months..."))

        if self.phone_no not in cust_info:
            cust_info[self.phone_no]=[self.name,self.age,self.gender,self.email,self.BMI,self.membershipDuration]
            
            self.Regimen(self.BMI,self.phone_no)
        
            print("\nMember added successfully...\n ")

        else:
            print("\nPhone no. already exist...\n ")

        time.sleep(2)
        self.admin_menu()
    


    def viewMember(self):
        if cust_info !={}:
            self.phoneNo=int(input("Enter phone no member ..."))
            
            if self.phoneNo in cust_info:
                print ("Details of member with phone no.",self.phoneNo)
                print ("\nName of Member...",cust_info[self.phoneNo][0])
                print ("Age of Member...",cust_info[self.phoneNo][1])
                print ("Gender of Member...",cust_info[self.phoneNo][2])
                print ("Email of Member...",cust_info[self.phoneNo][3])
                print ("BMI of Member...",cust_info[self.phoneNo][4])
                print ("Membership Duration of Member...",cust_info[self.phoneNo][5])

            else:
                print("\nIncorrect Phone No...\n ")


        else:
            print("\nYou do not have any data...\n ")


        time.sleep(2)
        self.admin_menu()


        
    def delMember(self):
        if cust_info !={}:
            self.phoneNo=int(input("Enter phone no member ..."))
            
            if self.phoneNo in cust_info:
                cust_info.pop(self.phoneNo)
                print("Member Removed Successfully...")

            else:
                print("\nPlease enter the correct phone no....\n")


        else:
            print("\nYou do not have any data...\n")


        
        time.sleep(2)
        self.admin_menu()


    def updateMember(self):
        if cust_info !={}:
            self.phoneNo=int(input("Enter phone no member ..."))
            
            if self.phoneNo in cust_info:
                print("\nThis is the previous record of the member...")

                print ("\nName of Member...",cust_info[self.phoneNo][0])
                print ("Age of Member...",cust_info[self.phoneNo][1])
                print ("Gender of Member...",cust_info[self.phoneNo][2])
                print ("Email of Member...",cust_info[self.phoneNo][3])
                print ("BMI of Member...",cust_info[self.phoneNo][4])
                print ("Membership Duration of Member...",cust_info[self.phoneNo][5])

                print ('\nPlease choose from following option to update.\n')
                
                print ( '1.Name\n2.Age\n3.Gender\n4.Email\n5.BMI\n6.Membership Duration\n' )
                choose = int(input())
                                
                if choose==1:
                    self.name=input("Enter new name...")
                    cust_info[self.phoneNo][0]=self.name
                    print("Name updated successfully")

                elif choose==2:
                    self.age=int(input("Enter new age..."))
                    cust_info[self.phoneNo][1]=self.age
                    print("Age updated successfully")

                elif choose==3:
                    self.gender=input("Enter correct gender...")
                    cust_info[self.phoneNo][2]=self.gender
                    print("Gender updated successfully")

                elif choose==4:
                    self.email=input("Enter new Email Address...")
                    cust_info[self.phoneNo][3]=self.email
                    print("Email updated successfully")

                elif choose==5:
                    self.bmi=int(input("Enter new BMI..."))
                    cust_info[self.phoneNo][4]=self.bmi
                    print("BMI updated successfully")

                elif choose==6:
                    self.md=int(input("Enter new Membership Duration..."))
                    cust_info[self.phoneNo][5]=self.md
                    print("Membership Duration updated successfully")

            else:
                print("you have entered the incorrect Phone no.")

        else:
            print("Sorry you don't have any member... please add some member... ")

                                        
        time.sleep(2)
        self.admin_menu()


    def regCreate(self):
        if cust_regimen !={}:
            self.phoneNo=int(input("Enter phone no member ..."))
            
            if self.phoneNo in cust_regimen:
                print("Create new Regimen of the Member...")
                cust_regimen[self.phoneno] = {
                'Mon' : input('Monday..') ,
                'Tue' : input('Tuesday') ,
                'Wed' : input('Wednesday') ,
                'Thu' : input('Thursday'),
                'Fri' : input('Friday') ,
                'Sat' : input('Saturday') ,
                'Sun' : input('Sunday')
                }

                print("Regimen created successfully...")

            else:
                print("Incorrect Phone No...")

        else:
            print("No data Found... Please add some members first...")


        time.sleep(2)
        self.admin_menu()



    def regView(self):
        if cust_regimen !={}:
            self.phoneNo=int(input("Enter phone no member ..."))
            
            if self.phoneNo in cust_regimen:
                for key,value in (cust_regimen[self.phoneNo].items()):
                    print(key,"==",value)

            else:
                print("Incorrect Phone No....")

        else:
            print("No data Found... Please add some members first...")


        time.sleep(2)
        self.admin_menu()



    def regDel(self):
         if cust_regimen !={}:
            self.phoneNo=int(input("Enter phone no member ..."))
            
            if self.phoneNo in cust_regimen:
                sureity=input("Are you sure you want to delete this Regimen...\nSelect 'Y' for yes and 'N' for no...")
                if sureity.upper=="Y":
                    cust_regimen[self.phoneno]= None
                    print("Regimen deleted successfully...")

                elif sureity.upper=="N":
                    print("Okayyy....")

                else:
                    print("Please select properly... ")

            else:
               print("Incorrect Phone No...")

         else:
            print("No data Found... Please add some members first...")


         time.sleep(2)
         self.admin_menu()

                


    def regUpdate(self):
        if cust_regimen !={}:
            self.phoneNo=int(input("Enter phone no member ..."))
            
            if self.phoneNo in cust_regimen:
                print("Update Regimen of the Member...")
                cust_regimen[self.phoneno] = {
                'Mon' : input('Monday..') ,
                'Tue' : input('Tuesday') ,
                'Wed' : input('Wednesday') ,
                'Thu' : input('Thursday'),
                'Fri' : input('Friday') ,
                'Sat' : input('Saturday') ,
                'Sun' : input('Sunday')
                }

                print("Regimen updated successfully...")

            else:
                print("Incorrect Phone No...")

        else:
            print("No data Found... Please add some members first...")


        time.sleep(2)
        self.admin_menu()


    def mem_profile(self):
        self.phoneNo=int(input("Enter phone no member ..."))
            
        if self.phoneNo in cust_info:
            print ("Details of member with phone no.",self.phoneNo)
            print ("\nName of Member...",cust_info[self.phoneNo][0])
            print ("Age of Member...",cust_info[self.phoneNo][1])
            print ("Gender of Member...",cust_info[self.phoneNo][2])
            print ("Email of Member...",cust_info[self.phoneNo][3])
            print ("BMI of Member...",cust_info[self.phoneNo][4])
            print ("Membership Duration of Member...",cust_info[self.phoneNo][5])

        else:
            print("\nIncorrect Phone No...\n ")


        time.sleep(2)
        self.member_menu()



    def mem_regimen(self):

        try:
            self.phoneNo=int(input("Enter phone no member ..."))
                
            if self.phoneNo in cust_regimen:
                for key,value in (cust_regimen[self.phoneNo].items()):
                     print(key,"==",value)

            else:
                print("Incorrect Phone no...")

        except ValueError:
            print("Enter proper mobile no.")

        time.sleep(2)
        self.member_menu()


    

def start() :
    print ( '****Welcome to Gym****' )
    obj = GYM ( )  # obj creation
    print ( '\nEnter your user type.\n' )
    types = input ( 'Enter "A" for admin, "M" for member:' )

    def admin_Login() :
        print("Please enter username:")
        username = input ( 'Username: ' )  # default = admin
        print("Please enter your password:")
        password = input ( 'Password: ' )  # default = admin

        if username == 'admin' and password == 'admin' :

            obj.admin_menu ( )  # showning admin menu 
        else :
            print ( '\nInvalid username and password.\n' )
            choice = input ( '\nDo you wish to try again? (Y/N)' )
            if choice.upper ( ) == 'Y' :
                admin_Login ( )
            elif choice.upper( ) == 'N' :
                start ( )
            else :
                print ( "\nInvalid option.\nLet's start again.\n" )
                start ( )


    def member_login() :
        phoneno=int(input("Enter your phone no as username...\nUsername:"))
        password=input("Enter your name as your password...\nPassword:")

        if phoneno in cust_info:
            if password == cust_info[phoneno][0]:
                obj.member_menu()  # showing Member menu

            else:
                print("Incorrect password...\nPlease try again..")
                member_login()
        else:
           print ( '\nInvalid username and password.\n' )
           choice = input ( '\nDo you wish to try again? (Y/N)' )
           if choice.upper ( ) == 'Y' :
                member_login ( )
           elif choice.upper( ) == 'N' :
                start ( )
           else :
                print ( "\nInvalid option.\nLet's start again.\n" )
                start ( )
        

                                     
                                        
    
    def start_option(types) :
        if types.upper ( ) == 'A' :
            admin_Login ( )
        elif types.upper ( ) == 'M' :
            member_login ( )
        else :
            print ( '\nWrong input.' )

        choice = input ( '\nDo you wish to login again? (Y/N)\n' )
        if choice.upper ( ) == 'Y' :
            types = input ( 'Admin/Member (A/M): ' )
            start_option ( types )
        elif choice.upper ( ) == 'N' :
            print ( '\nThanks for visiting....\nHope to see you soon....' )
        else :
            print ("\nInvalid option....\nPlease select an appropriate option...\nLet's do it again....\n\n" )
            start()

    start_option ( types )


start ( )

            

        


    
                    
        

                


