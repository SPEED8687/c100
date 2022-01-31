class ATM :
    def __init__(self,balance,cardNumber,pin) :
        self.balance=balance
        self.cardNumber=cardNumber
        self.pin=pin
    def checkBalance(self) :
        print("Your balance is",str(self.balance))
    def withdraw(self,amt) :
        if(amt>self.balance) :
            print("Insuffiect balance")
        else :
            self.balance=self.balance-amt
            print("The new balance is",str(self.balance))
    def deposit(self,amt) :
        self.balance=self.balance+amt
        print("The new balance is",str(self.balance))

john=ATM(100,"abc","1234")
john.checkBalance()
john.withdraw(50)
john.deposit(10)
    