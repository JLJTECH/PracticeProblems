#Return: a 'Yes' string for true and a 'No' string for false
def bool_to_word(bool):
    if bool == True:
        return "Yes"
    return "No"

#Alternate Solution
def bool_to_word(bool):
    return "Yes" if bool else "No"