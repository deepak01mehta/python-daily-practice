class Atm:

    def __init__(self):
        self.pin = ''
        self.balance = 10000
        self.UserName =''
        self.menu()

    def menu(self):
        UserInput = input(
            """
        Hi, how can I help you?
        1. Create pin
        2. Change pin
        3. Check balance
        4. Money withdraw
        5. Exit
            """
        )

        if UserInput == '1':
            self.create_pin()
        elif UserInput == '2':
            self.chnage_pin()

        elif UserInput == '3':
            self.check_amount()
            
        elif UserInput == '4':

            self.money_withdraw()
        else:
            #exit
            pass
#create Atm pin

    def create_pin(self):
        user_pin = input("Enter your pin")
        self.pin =user_pin

        user_name =input("Enter your name ")

        self.UserName = user_name

        print("pin crated successfully ",self.UserName)
        self.menu()
#chnage atm pin

    def chnage_pin(self):
        old_pin = input("Enter your old pin")

        if old_pin == self.pin:
            new_pin = input("Enter the new pin ")

            self.pin = new_pin
            print("pin chnage successfully")
            self.menu()
        
        elif old_pin != self.pin:

            again_old_pin = input("plz Enter the correct pin only ")
            if again_old_pin == self.pin:
                a_new_pin = input("enter the new pin ")
                self.pin = a_new_pin

                print("pin chnage successfully ")
                
                self.menu()

        

            
            
        else:
            print("dekh bhai sahi pin daal nhi to kuch or kar ye le menu  ")
            self.menu()


# check balence
    def check_amount(self):
        amount_pin = input("enter your pin")

        if amount_pin == self.pin:
            print("your amount",self.balance)
        else:
            print("wrong pin")
            self.menu()



    def money_withdraw(self):
        amount_pin = input("enter your  pin")

        if amount_pin == self.pin:
            amount = int(input("Enter you amount"))

            if amount <= self.balance:
                self.balance = self.balance -amount

                print("withdrawal successfully  balance is ",self.balance)

            else:
                print("garib saale")

        else:
            print("pin is incorrect")

            self.menu()



obj = Atm()


        
















            

