from Strategies.Account import Account

share_price = 100.0
account = Account()

def check_value(expected):
    global account, share_price
    return account.value(share_price) == expected

def check_shares(expected):
    global account
    return account.get_shares() == expected

def check_balance(expected):
    global account
    return account.get_balance() == expected

print "Share Price:", share_price
print "Starting Value, expect 0:", account.value(share_price)

success = check_value(0)
    
print "\nAdding $5000 to account balance."
account.increase_balance(5000)
print "Value, expect 5000:", account.value(share_price)

if success:
    success = check_value(5000)

print "\nAdding 2 share to account."
account.increase_shares(2)
print "Value, expect 5200:", account.value(share_price)

if success:
    success = check_value(5200)

print "\nSell 1 share."
account.sell(share_price, 1)
print "Shares, expect 1:", account.get_shares()
print "Value, expect 5200:", account.value(share_price)

if success:
    success = check_shares(1) and check_value(5200)

print "\nSell all shares."
account.sell(share_price)
print "Shares, expect 0:", account.get_shares()
print "Value, expect 5200:", account.value(share_price)

if success:
    success = check_shares(0) and check_value(5200)

print "\nBuy 1 share."
account.buy(share_price, 1)
print "Balance, expect 5100:", account.get_balance()
print "Value, expect 5200:", account.value(share_price)

if success:
    success = check_balance(5100) and check_value(5200)
    
print "\nBuy all shares."
account.buy(share_price)
print "Balance, expect 0:", account.get_balance()
print "Value, expect 5200:", account.value(share_price)

if success:
    success = check_balance(0) and check_value(5200)

if success:
    print "\nSUCCESS!"
else:
    print "\nFAILURE!"