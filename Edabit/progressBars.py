#!/usr/bin/env python3

'''
Create progress bars with the given symbol & Value combination.
'''

def progress_bar(bar, progress):
    #print("|" + " " * (10 - (progress//10)) + "|")
    if progress == 100:
        print("|" + (str(bar) * (progress // 10)) + "|" + " Completed!")
    else:
        print("|" + (str(bar) * (progress // 10)) + " " * (10 - (progress//10)) + "|" + " Progress: " + str(progress) + "%")

#Tests
progress_bar("=", 10) # "|=         | Progress: 10%")
progress_bar("#", 90) # "|######### | Progress: 90%")
progress_bar("*", 100) # "|**********| Completed!")
progress_bar("#", 50) # "|#####     | Progress: 50%")
progress_bar("*", 60) # "|******    | Progress: 60%")
progress_bar("#", 100) # "|##########| Completed!")
progress_bar("*", 60) # "|******    | Progress: 60%")
progress_bar("=", 30) # "|===       | Progress: 30%")
progress_bar(">", 70) # "|>>>>>>>   | Progress: 70%")
progress_bar("=", 40) # "|====      | Progress: 40%")
progress_bar(">", 20) # "|>>        | Progress: 20%")
progress_bar("*", 0) # "|          | Progress: 0%")
progress_bar("=", 60) # "|======    | Progress: 60%")
progress_bar(">", 90) # "|>>>>>>>>> | Progress: 90%")
progress_bar("*", 80) # "|********  | Progress: 80%")
progress_bar("#", 20) # "|##        | Progress: 20%")
progress_bar("*", 30) # "|***       | Progress: 30%")
progress_bar("=", 70) # "|=======   | Progress: 70%")
progress_bar("=", 0) # "|          | Progress: 0%")
progress_bar(">", 100) # "|>>>>>>>>>>| Completed!")
