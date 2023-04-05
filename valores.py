import math
nome = 'Gabriel'
print('Boa Noite {}{}{}'.format('\033[4;35m', nome, '\033[m'))
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
if n1 > n2 and n1 > n3:
    print(' \033[1;33;47mO maior valor foi {}\033[m'.format(n1))
elif n2 > n1 and n2 > n3:
    print(' \033[1;33;47mO maior valor foi {}\033[m'.format(n2))
elif n3 > n1 and n3 > n2:
    print(' \033[1;33;47mO maior valor foi {}\033[m'.format(n3))
if n1 < n2 and n1 < n3:
    print('\033[1;33;47mO menor valor foi {}\033[m'.format(n1))
elif n2 < n1 and n2 < n3:
    print('\033[1;33;47mO menor valor foi {}\033[m'.format(n2))
else:
    print('\033[1;33;47mO menor valor foi {}\033[m'.format(n3))