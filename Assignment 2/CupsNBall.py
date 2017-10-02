print('Words: A-B-C')
inp = input('Word(s): ').upper()
opaque_cup_1 = 1
opaque_cup_2 = 0
opaque_cup_3 = 0
# '=1' == 'ball'
for a in inp:
    if a == 'A':
        opaque_cup_1 = opaque_cup_1 ^ opaque_cup_2
        opaque_cup_2 = opaque_cup_2 ^ opaque_cup_1
        opaque_cup_1 = opaque_cup_1 ^ opaque_cup_2
    elif a == 'B':
        opaque_cup_2 = opaque_cup_2 ^ opaque_cup_3
        opaque_cup_3 = opaque_cup_3 ^ opaque_cup_2
        opaque_cup_2 = opaque_cup_2 ^ opaque_cup_3
    elif a == 'C':
        opaque_cup_1 = opaque_cup_1 ^ opaque_cup_3
        opaque_cup_3 = opaque_cup_3 ^ opaque_cup_1
        opaque_cup_1 = opaque_cup_1 ^ opaque_cup_3
if inp != 'A' and inp != 'B' and inp !='C':
    print ('Error, word not found')
elif opaque_cup_1 == 1:
    print ('The Ball is in the Cup 1')
elif opaque_cup_2 == 1:
    print ('The Ball is in the Cup 2')
elif opaque_cup_3 == 1:
    print ('The Ball is in the Cup 3')
