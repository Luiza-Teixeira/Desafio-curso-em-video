from math import sqrt
oposto = float(input('Qual valor do cateto oposto: '))
adjacente = float(input('Qual o valor do cateto adjacente: '))
hipotenusa = sqrt(oposto**2 + adjacente**2)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
#OU

from math import hypot
oposto = float(input('Qual valor do cateto oposto: '))
adjacente = float(input('Qual o valor do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))

