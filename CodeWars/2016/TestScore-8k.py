#Compare your score to the avg class score
def better_than_average(class_points, your_points):
    return int(your_points) > int(sum(class_points) / (len(class_points)))

