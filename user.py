class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    
    def make_widthdrawl(self,amount):
        if self.account_balance < 0:
            print("There is no money to widthdraw")
        else:
            self.account_balance -= amount
            return self
    
    def display_user_balance(self):
        amount = self.account_balance
        print(self.name,"you have a total balance of",amount)
        return self

angelo = User("Angelo","angelo@python.com")
kathy = User("Kathy","kathy@python.com")
kendrick = User("Kendrick", "kendrick@python.com")

angelo.make_deposit(100).make_deposit(100).make_deposit(50).display_user_balance().make_widthdrawl(200).display_user_balance()
kathy.make_deposit(90).make_deposit(220).display_user_balance().make_widthdrawl(90).make_widthdrawl(5).display_user_balance()
kendrick.make_deposit(10).make_widthdrawl(100).make_widthdrawl(100).make_widthdrawl(100).display_user_balance()