from functions import Math
print('-'*30)
print('Welcome to the newest ultimate simple Calculator Pro v2.0!!')
print('-'*30)

while True:
    print('-'*30)
    print('1. Sum')
    print('2. Subtraction')
    print('3. Multplication')
    print('4. Division')
    print('5. Exponation')
    print('6. Squared number')
    print('7. Exit')
    op = int(input('>> '))
    print('-'*30)

    if op == 1:
      a = float(input('First number: '))
      b = float(input('Second number: '))
      print(Math.numSum(a, b))

    elif op == 2:
        a = float(input('First number: '))
        b = float(input('Second number: '))
        print(Math.numSubt(a, b))

    elif op == 3:
        a = float(input('First number: '))
        b = float(input('Second number: '))
        print(Math.numMult(a, b))

    elif op == 4:
        a = float(input('First number: '))
        b = float(input('Second number: '))
        print(Math.numDiv(a, b))

    elif op == 5:
        a = float(input('First number: '))
        b = float(input('Second number: '))
        print(Math.numExpo(a, b))

    elif op == 6:
        a = float(input('>> '))
        print(Math.numSRoot(a))

    elif op == 7:
        break

    else:
        print('Command not found!')


