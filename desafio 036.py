preço = float(input('Qual o valor do imóvel que deseja comprar:R$'))
salario = float(input('Informe o valor do seu salário:R$'))
prazo = float(input('Em quantos anos pretende pagar esse imovél?\n'))
prestação = (preço / (prazo * 12))
if prestação > 0.3 * salario:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
