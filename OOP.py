
# a bank object
class Account:
    def __init__(self):
        self.name = 'Your Name'
        self.branch = 'Waiyaki way'
        self.age = 10
        self.accno = 1000050
        self.balance = 50
        # we define the atributes of states of your account


    # behavior deposit, withdraw, buyairtime, checkbalance, takeloan
    def deposit(self, amount):
        print('Welcome ', self.name)
        print('Your Current Balance is ', self.balance)
        self.balance = self.balance + amount
        print('You deposited ', amount)
        print('Your New balance is ', self.balance)
        print('Thank you')
     # withdrawal

    def withdraw(self, amount):
        print('Welcome ', self.name)
        print('Your Current balance is ', self.balance)
        if amount > self.balance:
            print('You have insufficient Funds')
            



















object = Account()  # instantiate
object.deposit(2000)
object.deposit(2000)
# Assignment
# do a withdrawal function, if possible check that we can't withdraw more than balance
#                  if possible check we can't withdraw a zero
                   # Hint.. use if statements
# do a checkbal function



