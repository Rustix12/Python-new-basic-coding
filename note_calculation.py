p = int(input("Enter the amount of taka: "))

k = p//1000

print("Thousand taka notes: ",k)

p = p%1000

h5 = p//500

print("Five hundred taka notes: ",h5)

p = p%500

h2 = p//200

print("Two hundred taka notes: ",h2)

p = p%200

h1 = p//100

print("One hundred taka notes: ",h1)

p = p%100

f = p//50

print("Fifty taka notes: ",f)

p = p%50

t = p//20

print("Tweanty taka notes: ",t)

p = p%20

t1 = p//10

print("Ten taka notes: ",t1)

p = p%10

f1 = p//5

print("Five taka notes: ",f1)

p = p%5

t1 = p//2

print("Two taka notes: ",t1)

p = p%2

print("One taka notes: ",p)
