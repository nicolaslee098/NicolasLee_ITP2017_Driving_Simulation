def abc ():
    class app:
        def __init__(self, app):
            self.app = app
        def phone (self):
            self.phone = input('Do you want to open an app?')

    class game:
        def __init__(self, game):
            self.game=0
        def phone1(self):
            self.phone1=input('Do you want to open a game?')

    while True:
        list = ['game','application']
        print ('Phone Actions: 1. Game, 2. Application\nWhat do you want to do with your phone(1/2)?')
        v = input ().lower().strip()
        if v == '1':
            x=app
            x.phone
            a = input('What app: ')
            print ('Opening ' + (a))
            print ((a)+' opened.')
        elif v == '2':
            y=game
            y.phone1
            b = input('What game: ')
            print ('Opening ' + (b))
            print ((b)+' opened')
            print ((b)+' is the greatest game.')
        print('Do you still want to use the phone(Y/N)?')
        q = input().lower().strip()
        if q == 'y':
            print ()
        elif q =='n':
            break
abc()
