import unittest
from Strategies.Account import Account

SHARE_PRICE = 100.0

class TestAccount(unittest.TestCase):
    account = Account()
    
    def test_1_inital_value(self):
        self.assertEqual(self.account.value(SHARE_PRICE), 0, "default init account value")
        
    def test_2_adding_money(self):
        self.account.increase_balance(5000)
        self.assertEqual(self.account.value(SHARE_PRICE), 5000, "increase balance 5000")
        
    def test_3_add_shares(self):
        self.account.increase_shares(2)
        self.assertEqual(self.account.value(SHARE_PRICE), 5200, "increase 2 shares")
    
    def test_4_buy_shares(self):
        self.account.buy(SHARE_PRICE,1)
        self.assertEqual(self.account.get_shares(), 3, "buy 1 share - check shares")
        self.assertEqual(self.account.get_balance(), 4900, "buy 1 share - check balance")
        self.assertEqual(self.account.value(SHARE_PRICE), 5200, "buy 1 share - check balance")
        
        self.account.buy(SHARE_PRICE)
        self.assertEqual(self.account.get_balance(), 0, "buy as many shares - balance")
        self.assertEqual(self.account.value(SHARE_PRICE), 5200, "buy as many shares - value")
        
    def test_5_sell_shares(self):
        self.account.sell(SHARE_PRICE, 1)
        self.assertEqual(self.account.get_shares(), 51, "sell 1 share - check shares")
        self.assertEqual(self.account.value(SHARE_PRICE), 5200, "sell 1 share - check value")
        
        self.account.sell(SHARE_PRICE) # sell all shares
        self.assertEqual(self.account.get_shares(), 0, "sell all shares - check shares")
        self.assertEqual(self.account.value(SHARE_PRICE), 5200, "sell all shares - check value")

    def test_6_exceptions(self):
        self.assertRaises(ValueError, self.account.buy, SHARE_PRICE, 5000)
        self.assertRaises(ValueError, self.account.sell, SHARE_PRICE, 10000)


        

