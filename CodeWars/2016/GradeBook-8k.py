#Complete the function so that it finds the mean of the three scores passed to it and returns the letter value associated with that grade.
def get_grade(s1, s2, s3):
    sg = (s1 + s2 + s3) / 3
    if sg >= 90:
        return "A"
    elif sg >= 80:
        return "B"
    elif sg >= 70:
        return "C"
    elif sg >= 60:
        return "D"
    else:
        return "F"
        
#Alternate Solution
def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')
