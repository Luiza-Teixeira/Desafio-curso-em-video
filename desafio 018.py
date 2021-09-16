import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o seno {:.2f}'.format(angulo,seno))
print('O ângulo de {} tem o cosseno {:.2f}'.format(angulo,cosseno))
print('O ãngulo de {} tem a tangente {:.2f}'.format(angulo, tangente))

#OU

from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o seno {:.2f}'.format(angulo,seno))
print('O ângulo de {} tem o cosseno {:.2f}'.format(angulo,cosseno))
print('O ãngulo de {} tem a tangente {:.2f}'.format(angulo, tangente))
