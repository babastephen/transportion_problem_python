import numpy as np
import trans as ts

cost = []
a = []
i = 1
j = 1
# for i in range(3):
q=int(input("Row Number :"))
b=int(input("Column Number :"))
def ya():
    global i
    global j
    global a
    if i <= q:
        costs = int(input("Enter values "))
        a.append(costs)
        j = j + 1
        if j > b:
            cost.append(a)
            i = i + 1
            j = 1
            a = []
        ya()
ya()
ts.userCostInput.costs = cost
ts.userCostInput()
#print(ts.userCostInput.costs)
#ts.userCostInput()
