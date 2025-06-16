b = float(input("Enter the buying price: "))

s = float(input("Enter the selling price: "))

if b < s:
    print("Profit of tk. ",s-b)
elif b == s:
    print("No profit , no loss")
else:
    print("Loss of tk. ",b-s)