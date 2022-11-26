import random
print ('======================================= \n'
       '        Jogo da Adivinhação \n'
       '=======================================')
n2 = int(input('Qual número eu to pensando de 0 a 5:'))
n1 = random.randint(0,5)#vai gerar número aleatório de 0 a 5
if n1 == n2:
    print('Você Ganhou Parabens!!!')
else:
    print('Você Perdeu, o número sorteado foi {}. Tente novamente'.format(n1))