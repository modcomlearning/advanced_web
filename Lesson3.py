
# Declare variables to store   gross income, and number of children.
# Each taxpayer's tax due is computed as follows;
# The taxpayer's dependency exemption is determined by multiplying $3,000 times the number of children.
# The taxpayer's net income is determined by taking the taxpayer's gross income
# and subtracting the taxpayer's dependency exemption.
# if netpay < 50000, tax is 15% of salary
# 50000  - 70000    tax 20% of salary
# over 70000 pay 25% of salary

def check(net_income): # expecting a net income
    if net_income < 50000:
        print('Tax will be 15% of ', net_income)

    elif net_income < 70000:
        print('Tax will be 20% of', net_income)

    elif net_income < 100000:
        print('Tax will be 25% of', net_income)

    else:
        print('Tax will be 30% of ', net_income)

def employee_tax():
    gross_income = 50000
    number_of_children = 2

    # get dependency exemption
    dependency_exemption  = number_of_children * 3000
    print('Dependency Exemption', dependency_exemption)

    net_income = gross_income - dependency_exemption
    print('Net Income KES', net_income)

    # Re use a function in lesson2a
    from Lesson2a import converter
    print('Net Income in USD ', converter(net_income))
    check(net_income)  # provides the net_income to check()
    # Here we learn that code is improved when functions are used.i,e converter is re used
    # DRY - Don't Repeat Yourself
    # Control Statements.. if, elif, else , for , while


#
employee_tax()