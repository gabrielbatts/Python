from datetime import date
ano = date.today().year
anoNascimento = int(input('Qual é o ano de seu nascimento? '))
idade = int( ano - anoNascimento)
if idade == 18 or idade == 17:
    print('Você está na idade para se alistar')
elif idade < 16:
    print('Você ainda não tem idade para se alistar')
else:
    print('Você já passou da idade para se alistar. \n Você pagará uma multa')