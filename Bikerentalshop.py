class bikeShop:
   
    def __init__(self, stock):
        self.stock = stock
    
    #Displaying the Stocks of Bikes
    def displayBike(self):
        print("Total Bikes",self.stock)
    
    # Renting the Bikes
    def rentForBike(self, q):
        if q <=0:
            print("Enter the Positive value or Greater than 0")
        
        if q > self.stock:
            print("Enter the quantity lesser than the available stocks : ",self.stock)
        
        else:
            print("Total Price ", q*100)
            print("Total Bikes Available", self.stock)

while True:
    obj = bikeShop(100)
    userChoice = int(input('''
1 Display Stocks
2 Rent a Bike
3 Exit
        '''))
    if userChoice == 1:
        obj.displayBike()
    elif userChoice == 2:
        n = int(input("Enter the quantity: ---"))
        obj.rentForBike(n)
    else:
        break 