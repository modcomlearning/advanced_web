
# Declare variables to store   gross income, and number of children.
# Each taxpayer's tax due is computed as follows;
# The taxpayer's dependency exemption is determined by multiplying $3,000 times the number of children.
# The taxpayer's net income is determined by taking the taxpayer's gross income
# and subtracting the taxpayer's dependency exemption.
def employee_tax():
    gross_income = 50000
    number_of_children = 2

    # get dependency exemption
    dependency_exemption  = number_of_children * 3000
    print('Dependency Exemption', dependency_exemption)

    net_income = gross_income - dependency_exemption
    print('Net Income KES', net_income)




employee_tax()