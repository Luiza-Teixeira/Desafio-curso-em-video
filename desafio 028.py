from random import randint
while 1:
    pc = randint(0,5)# Faz o computador "pensar"
    jogador = input('Qual o valor de 0 a 5 o pc pensou?')
    if jogador == pc:
        print('Você ganhou! Parabéns')
    else:
        print('Você perdeu! hahahaha')
        print('Eu pensei no número {} e não no {}'.format(pc, jogador))



    
