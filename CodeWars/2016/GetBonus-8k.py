#If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money and must receive only his stated salary.
def bonus_time(salary, bonus):
    if bonus == True:
        return "$" + str(salary * 10)
    else:
        return "$" + str(salary)

#Alternate Solution
def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1))