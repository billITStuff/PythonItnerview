#Check if list contains integer

mylst = [1,3,5,7,8,10,110,9]
number1 = 3
number2 = 12

def list_contains(num, lst):
        if num in lst:
            print(f"The number {num} is in the list.")
        else:
            print(f"The number {num} is not in the list.")

list_contains(number1, mylst)
list_contains(number2, mylst)

#find Max and Min

def list_Max_Min(lst):
        print("The max is: ", max(lst))
        print("The min is: ", min(lst))

list_Max_Min(mylst)