#List of randoms

import random
import math

numList = []

for i in range(10):
    numList.append(random.randrange(1, 20))

for i in numList:
    print("Rand num = " + str(i))
