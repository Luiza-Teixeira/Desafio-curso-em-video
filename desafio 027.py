nome = input('Digite seu nome completo:\n').upper().strip().split()
print('Olá {}, prazer te conhecer!'.format(nome))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1))
      #ou
#print('Seu último nome é: {}'.format(nome[-1]))      

