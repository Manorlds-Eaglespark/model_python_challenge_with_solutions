# QN4
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


def account_balance(deposits, withdrawals):
    total_W = 0
    total_D = 0
    for d in deposits:
        total_D += d
    for w in withdrawals:
        total_W =+ w
    balance = total_D - total_W
    return balance

deposits = [300, 300, 100]
withdrawals = [200]
print(account_balance(deposits, withdrawals))