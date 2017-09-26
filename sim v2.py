u = 0
speed_limit = 60
t = int (input('Time: '))
a = int (input('Acceleration: '))
d = int (input('Distance: '))
s = d/t
v = u + ( t * a )
for i in range (t):
    displacement = (a * (i ** 2)/2)
    x = int(displacement/10) * "*"
    print ('Duration:'+ " " +str(i) , 'distance: ' + ' '+str(x))
if s > speed_limit:
    print ('The person went over the speed limit. (Max speed was ' + (str(s)) + ' m/s)')
else:
    print ('The person did not go over the speed limit. (Max speed was ' + (str(s)) + ' m/s)')
if d > (int(displacement)):
    print ('The person reached the destination. (Reached' + (str(displacement))+ 'm)')
else:
    print ('The person did not reach the destination. (Reached ' + (str(displacement))+ ' m)')
