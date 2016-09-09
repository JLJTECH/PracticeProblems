#Make a function that receive age, and return what they drink.
def people_with_age_drink(age):
    if age <= 13:
        return "drink toddy"
    elif age <= 17:
        return "drink coke"
    elif age <= 18:
        return "drink beer"
    elif age <= 20:
        return "drink beer"
    elif age <= 30:
        return "drink whisky"
    else:
        return "drink toddy"
#Alternate Solution
def people_with_age_drink(age):
    if age > 20: return 'drink whisky'
    if age > 17: return 'drink beer'
    if age > 13: return 'drink coke'
    return 'drink toddy'