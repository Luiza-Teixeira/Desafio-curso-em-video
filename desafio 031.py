distancia = float(input('Digite o valor em Km da distância que será percorrida:\n'))
if distancia <= 200:
    print('O valor da passagem é:\n {}'.format(distancia*0.50))
else:
    print('O valor da passagem é:\n {}'.format(distancia*0.45))
