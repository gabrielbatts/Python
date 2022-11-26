print('-=-'*20)
vel = int(input('Diga a velocidade atual do carro: '))
if vel > 80:
    vel = vel - 80
    vel = vel * 7
    print('Você foi multado! multa de {:.2f} R$ diriga com segurança'.format(vel))
else:
    print('Tenha um bom dia! Diriga com segurança')