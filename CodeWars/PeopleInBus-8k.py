#Count remaining people on bus.
def number(bus_stops):
    a = sum(i[0] for i in bus_stops)
    b = sum(i[1] for i in bus_stops)
    return a - b

#Code Variation
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
