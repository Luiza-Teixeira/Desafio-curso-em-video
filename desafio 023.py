
numero = int(input('Digite um número de 0 a 9999:\n'))
unidade = numero % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('unidade: {}, dezena: {}, centena: {} e milhar: {}'.format(unidade, dezena, centena, milhar))
