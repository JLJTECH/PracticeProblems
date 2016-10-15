#Write a function that returns a string in which firstname is swapped with last name.

def name_shuffler(str_):
    return ' '.join(str_.split()[::-1])