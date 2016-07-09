# Enter your code here. Read input from STDIN. Print output to STDOUT
m = float(raw_input());
t = m * input() /100;
x = m * input() /100;
totalCost = round(m + x + t);
print ('The total meal cost is' " " + str(int(totalCost)) + " " 'dollars.')