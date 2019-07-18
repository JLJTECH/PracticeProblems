#write a function that takes a String and returns an Array/list with the length of each word added to each element .

def add_length(str_):
    return ["{} {}".format(x, len(x)) for x in str_.split(' ')]