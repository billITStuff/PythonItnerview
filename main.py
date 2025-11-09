#Check if list contains integer

def list_contains(num, lst):
        if num in lst:
            print(f"The number {num} is in the list.")
        else:
            print(f"The number {num} is not in the list.")


mylst = [1,3,5,7,8,10,110,9]
number1 = 3
number2 = 12

list_contains(number1, mylst)
list_contains(number2, mylst)