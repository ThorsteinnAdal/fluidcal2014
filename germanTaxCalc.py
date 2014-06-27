step1 = 8004.
step2 = 13469.
step3 = 52881.
step4 = 250730.

def taxes(income):
    ''' Calculation of taxes to be paid for taxable income x'''
    if income <= step1:
        tax = 0
    elif income <= step2:
        y = (income - step1)/10000.
        tax = (912,17*y +1400)*y
    elif income <= step3:
        z = (income - step2)/10000.
        tax = (228.74*z + 2398.0)*z + 1038
    elif income <= step4:
        tax = income *0.44 - 8172.0
    else:
        tax = income *0.44 - 15694
    return tax
