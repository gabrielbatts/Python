print ('Calcule a distância de sua viagem')
dis = float(input('Digite qual a distancia em Km da sua viajem: '))

if dis>= 200:
    print('O preço da passagem é de {:.2f} R$'.format(dis*0.50))

else:
    print (' O preço da passagem é de {:.2f} R$'.format(dis*0.45))