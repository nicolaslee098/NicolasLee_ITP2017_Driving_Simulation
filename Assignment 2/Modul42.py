list = []
for inp in range (0,10): #to input numbers, max 10 inputs
    inp = int(input())
    a = inp % 42
list.append(a)
print(len(set(list)))
