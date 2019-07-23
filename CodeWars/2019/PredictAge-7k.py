#!/usr/bin/env python3
'''
Take a list of ages.
Multiply each number by itself. Add them all together. Take the square root of the result. Divide by two.
'''
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    import math
    x = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    c = [i * i for i in x]
    return (math.sqrt(sum(c))//2)

#Alternate Solutions
def predict_age(*ages):
    return sum(a*a for a in ages)**.5//2
