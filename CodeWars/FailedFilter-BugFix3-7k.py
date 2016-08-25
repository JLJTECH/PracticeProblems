#FilterNumber function to remove all the numbers from the string
def filter_numbers(string):
    return ''.join([i for i in string if not i.isdigit()])


