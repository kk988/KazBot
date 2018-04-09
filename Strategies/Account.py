from lib2to3.pgen2.token import PERCENT
class Account():
    def __init__(self, starting_balance=0, starting_shares=0):
        self.balance = float(starting_balance)
        self.shares = float(starting_shares)
        self.value_at_buy = 0
        
    def get_balance(self):
        return self.balance
    
    def get_shares(self):
        return self.shares
    
    def set_balance(self, balance):
        self.balance = balance
        
    def set_shares(self, shares):
        self.shares = shares
    
    def increase_balance(self, increase):
        self.balance += increase
        
    def increase_shares(self, increase):
        self.shares += increase
    
    def sell(self, share_price, shares_to_sell=None):
        if shares_to_sell:
            if shares_to_sell > self.shares:
                raise ValueError("Attempted to sell more shares than you own.")
        else:
            shares_to_sell = self.shares
        
        self.balance += shares_to_sell * share_price
        self.shares -= shares_to_sell
        self.shares = round(self.shares, 5)
        
        profit_loss = self.value(share_price) - self.value_at_buy
        percent_change = ( profit_loss / self.value_at_buy ) * 100
        
        print("P/L", profit_loss, "\tPercent Change:", percent_change, "%")
        
        
    
    def buy(self, share_price, shares_to_buy=None):
        if shares_to_buy:
            if shares_to_buy > (self.balance / share_price):
                raise ValueError("Attempted to purchase more shares than you can afford.")
        else:
            shares_to_buy = self.balance / share_price
        
        self.shares += shares_to_buy
        self.balance -= shares_to_buy * share_price
        self.balance = round(self.balance, 5)
        
        self.value_at_buy = self.value(share_price)

    def value(self, share_price):
        return self.balance + (self.shares * share_price)