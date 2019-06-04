class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
    
    def make_widthdrawl(self,amount):
        if self.account_balance < 0:
            print("There is no money to widthdraw")
        else:
            self.account_balance -= amount
    
    def display_user_balance(self):
        amount = self.account_balance
        print(self.name,"you have a total balance of",amount)

angelo = User("Angelo","angelo@python.com")
kathy = User("Kathy","kathy@python.com")
kendrick = User("Kendrick", "kendrick@python.com")

angelo.make_deposit(100)
angelo.make_deposit(100)
angelo.make_deposit(50)
angelo.display_user_balance()
angelo.make_widthdrawl(200)
angelo.display_user_balance()

kathy.make_deposit(90)
kathy.make_deposit(220)
kathy.display_user_balance()
kathy.make_widthdrawl(90)
kathy.make_widthdrawl(5)
kathy.display_user_balance()

kendrick.make_deposit(10)
kendrick.make_widthdrawl(100)
kendrick.make_widthdrawl(100)
kendrick.make_widthdrawl(100)
kendrick.display_user_balance()