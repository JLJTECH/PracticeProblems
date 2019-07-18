#Take in an input array containing the names of people who like an item
def likes(names):
    count = len(names[1:-1])
    if not names:
        return "no one likes this"
    elif len(names) == 3:
        return names[0] + ', '+ names[1]+' and '+names[2]+' like this'
    elif len(names) == 2:
        return names[0]+' and '+ names[1]+' like this'
    elif len(names) >= 4:
        return names[0] + ', '+ names[1]+' and '+ str(count) + ' others like this'
    else:
        return names[0]+' likes this'

#Alternate solution
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)