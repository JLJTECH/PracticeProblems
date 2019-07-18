#Return a count of all vowels in string
def getCount(inputStr):
    count = 0
    vowels = set("aeiou")
    for let in inputStr:
        if let in vowels:
            count += 1
    return count

#Alternate solution
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")