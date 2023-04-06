print('-=-'*20)
print('                   Banco Cripto')
print('-=-'*20)
casa = float(input('Qual o valor da casa que você quer comprar? '))
salario = float (input('Qual é o valor do seu salário? '))
ano = int (input('Vai pagar em quantos anos? '))
mes = ano * 12
prestaçao = float( casa / mes ) 
valorParcelaAprovado = float (salario * 30 / 100)
if prestaçao < valorParcelaAprovado:
    juros = float (prestaçao * 0.12)
    prestaçao += juros
    valorFinal = float(prestaçao * mes)
    print('O valor das prestações ficará {:.2f}R$ em {}x' .format(prestaçao, mes))
    print('O valor final ficará {:.2f}R$'.format(valorFinal))
else:
    print('O seu salário é incompatível para fazer esse empréstimo. ')
