
# Github  - create a github account - at the end of lesson .
# Functions and Control Statements
# Why Functions?
#  Widely Used in Most Frameworks
#  Widely used in Object Oriented Programming
#  They divide your big code into smaller modules or blocks
#  One function can perform a specific task


# Create a conversion function
# amount_in_kes is a parameter
def converter(amount_in_kes):
    # convert the amount received to usd
    amount_in_usd = amount_in_kes/108
    return amount_in_usd


# Google classroom: ptv4a6I
# 0729 225 710
def payroll():
    basic_salary = 50000
    allowances = 2000
    deductions = 3000

    # Find gross pay
    gross_pay = basic_salary + allowances
    print('Gross Pay is KES', gross_pay)
    # convert gross pay to usd
    print('Gross in Usd ', converter(gross_pay))


    # Find net pay
    net_pay = gross_pay - deductions
    print('Net Pay is KES', net_pay)
    # convert the netpay in usd
    print('Netpay in usd ', converter(net_pay))


# call a function for it to run
payroll()

