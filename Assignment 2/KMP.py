final = ''
w = input().upper() # or title to make the output uppercase
for a in w.split('-'):
    final += a[0]
print (final)
