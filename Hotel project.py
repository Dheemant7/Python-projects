class Hotel:

    def __init__(self,name='',address='',cindate='',coutdate='',roomno='',amt='',rent=0,fbill=0,chrg=" "):

        print ("*****                  *****")
        print ("      WELCOME TO HOTEL      ")
        print ("*****                  *****")
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.roomno=roomno
        self.amt=amt
        self.fbill=fbill
        self.rent=rent
        self.chrg=chrg

    def inputdata(self):
        self.name=input("Enter customer Name : ")
        self.address=input("Enter customer address : ")
        self.cindate=input("Enter check in date : ")
        self.coutdate=input("Enter checkout date : ")
        self.roomno=input("Enter room number : ")
        
    def roomrent(self):

        print ("We have the following rooms for you:-")
        print ("*** Type of Rooms ***     Rate ")
        print ("1. Standard          ---> 1000 ")
        print ("2. Deluxe(Non A/C)   ---> 2000 ")
        print ("3. Deluxe (A/C)      ---> 3000 ")
        print ("4. Suites            ---> 5000 ")

        x=int(input("Enter the number of choice Please -> "))

        n=int(input("For How Many Nights Did Customer Stay:"))

        if(x==1):

            print ("Customer have choosen Standard room ")
            self.rent=1000*n

        elif (x==2):

            print ("Customer have choosen Deluxe (Non A/C)room")
            self.rent=2000*n

        elif (x==3):

            print ("Customer have choosen Deluxe (A/C) room")
            self.rent=3000*n

        elif (x==4):
            print ("Customer have choosen Suite")
            self.rent=5000*n

        else:

                   print ("please choose a room")

        print ("Customer choosen room rent is =",self.rent)

    def restrobill(self):

        print("*****RESTAURANT MENU*****")

        print("1. Dessert   ---> 100 ")
        print("2. Drinks    ---> 70 ")
        print("3. Breakfast ---> 150 ")
        print("4. Lunch     ---> 200 ")
        print("5. Dinner    ---> 300 ")
        print("6.Exit")

        while 1:

            f=int(input("Enter the number of your choice:"))

            if f==1:
                d=int(input("Enter quantity of Dessert -: "))
                self.fbill+=100*d

            elif f==2:
                d=int(input("Enter quantity of Drink-: "))
                self.fbill+=70*d

            elif f==3:
                d=int(input("Enter quantity of Breakfast -: "))
                self.fbill+=150*d

            elif f==4:
                d=int(input("Enter quantity of Lunch:"))
                self.fbill+=200*d

            elif f==5:
                d=int(input("Enter the Dinner:"))
                self.fbill+=300*d

            elif f==6:
                break;
            else:
                         print("You've Enter an Invalid Key")

        print ("Total food Cost=Rs",self.fbill)

    def display(self):
        print("---------------------")
        print("      HOTEL BILL     ")
        print("---------------------")
        print(" ")
        print ("  Customer Details  ")
        print ("******       ******")
        print ("Customer name : ",self.name)
        print ("Customer address : ",self.address)
        print ("Check in date : ",self.cindate)
        print ("Check out date : ",self.coutdate)
        print ("Room no. : ",self.roomno)
        print ("Customer Room rent is : ",self.rent)
        print ("Customer Food bill is : ",self.fbill)

        self.amt=self.rent+self.fbill

        print ("Customer total amount w/o tax and charges : ",self.amt)
        if self.amt>5000 and self.amt<10000:
            self.chrg=self.amt*.10
            print ("Additional Tax & Service Charges are : ",self.chrg)
            print ("Customer grandtotal Purchased is:",self.amt+self.chrg,"\n")
        else:
            self.amt>10000 
            self.chrg=self.amt*.15
            print ("Additional Tax & Service Charges are : ",self.chrg)
            print ("Customer grandtotal Purchased is:",self.amt+self.chrg,"\n")

def main():
    chrg=Hotel()

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate Room Rent")

        print("3.Calculate Food Purchased")

        print("4.Show total Bill")

        print("5.EXIT")

        m=int(input("\nEnter the number of your choice:"))
        if (m==1):
            chrg.inputdata()
        if (m==2):

            chrg.roomrent()

        if (m==3):

            chrg.restrobill()

        if (m==4):

            chrg.display()
            
main()