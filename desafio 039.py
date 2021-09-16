anoNascimento = int(input('Digite o ano do seu nascimento: '))
anoatual = int(input('Digite o ano atual:'))
idade = anoatual - anoNascimento
idade_1 = 18 - idade
idade_2 = idade - 18
if idade == 18:
    print('Você precisa se alistar!')
if idade > 18:
    print('Você passou {}anos do prazo de se alistar.'.format(idade_2))
if idade < 18:
    print('Ainda falta {}anos pra você precisar de alistar.'.format(idade_1))
    

