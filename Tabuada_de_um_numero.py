#Este codigo resolve tabuadas de qualquer numero

x = int(input('Digite um numero para ver sua tabuada:'))
y = x
z = 1
print('-' * 12)

while z <= 10:
    print('{} x {:2} = {}' .format(y, z, y*z ))
    x -= z
    z += 1


print('-' * 12)
