
# Github  - create a github account - at the end of lesson .
# Functions and Control Statements
# Why Functions?
#  Widely Used in Most Frameworks
#  Widely used in Object Oriented Programming
#  They divide your big code into smaller modules or blocks
#  One function can perform a specific task






def payroll():
    basic_salary = 50000
    allowances = 2000
    deductions = 3000

    # Find gross pay
    gross_pay = basic_salary + allowances
    print('Gross Pay is KES', gross_pay)
    # convert gross pay to usd
    gross_in_usd = gross_pay/108
    print('Gross in USD is ', gross_in_usd)

    # Find net pay
    net_pay = gross_pay - deductions
    print('Net Pay is KES', net_pay)
    # convert the netpay in usd
    net_in_usd = net_pay/108
    print('Net Pay is USD ', net_in_usd)

# call a function for it to run
payroll()

