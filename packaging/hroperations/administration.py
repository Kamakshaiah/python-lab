def emp_email(fname, lname):
    ''' creates email '''
    import random
    empid = round(random.random()*100)
    email_ = fname + '.' + lname + '@email.com'
    return((empid, email_))

def biometric():
    ''' processes days for payroll '''
    import random
    absence = round(random.uniform(1, 5))
    attend_ = 30 - absence
    if absence > 3:
        print('leaves exceeds permissible limits.')
    return(attend_, absence)

def promotion():
    ''' promotion based on performance [cpr - cummulative performance rating] of the employee '''
    import random
    cpr = [i for i in random.choices(range(1, 5), k=12)]
    if sum(cpr) > 50:
        print('you are promoted to next level/')
    else:
        print('No promotion for time being. Good luck next cycle.')
    return(cpr, sum(cpr))

def demotion(cpr):
    if cpr[1] < 20:
        print('you are demoted!')
    elif cpr[1] > 20 and cpr[1] <40:
        print('your are in hitlist.')
    else:
        print('you are save otherwise.')
    
def leave_appli():
    ''' process leave application '''
    import random
    total_leaves = 12
    used_leaves = random.choice(range(1, 12))
    balance_leaves = total_leaves - used_leaves

    if balance_leaves >= 12:
        print("you can't apply for leaves")
    else:
        print('your leave is sanctioned')
        
    return(dict(total=total_leaves, used=used_leaves, balance=balance_leaves))

def transfer(cpr):
    if cpr[1] > 50:
        print('your are required in the current working place.')
    else:
        print('your application for promotion is submitted successfully. Will let you know anon!')
    return(cpr)

if __name__ == '__main__':
##    print(emp_email('kamakshaiah', 'musunuru'))
##    print(biometric())
    cpr = promotion()
##    demotion(cpr)
##    print(leave_appli())
    print(transfer(cpr))
