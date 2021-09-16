num = int(input('Digite um numero a ser convertido:'))
print('''Escolha qual conversão deseja:
[1] - Converter para BINÁRIO
[2] - Converter para OCTAL
[3] - Converter para HEXADECIMAL''')
opção = int(input('Digite qual conversão deseja realizar:'))
if opção == 1:
    print('{} em binário é:{}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} em octal é:{}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} em hexadecimal é:{}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
