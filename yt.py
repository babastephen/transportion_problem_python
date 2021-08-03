i=1
def Get_Cost_Values():
    global i
    global j

    if i < 9:
        a = input("enter :")
        print(a)

        i = i + 1
        Get_Cost_Values()
    else:
        print("no")
Get_Cost_Values()

