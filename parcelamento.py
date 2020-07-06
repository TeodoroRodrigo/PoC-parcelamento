print('### Este script foi feito em Python para calcular o valor de parcelas ###')

print('Qual o valor a ser parcelado?')
total = int(float(input())*100) #qualquer valor digitado após a 2a casa decimal será ignorado.
valorTotal = total/100
#print('O Valor Total a ser parcelado é R$ {}'.format(valorTotal))

print('Qual o número de parcelas?')
numParcelas = int(input())
#print('O número de parcelas é {}'.format(numParcelas))

parcela = total // numParcelas
valorParcela = parcela/100

resto = (total) % numParcelas
#print('O Resto é {}'.format(resto))

if resto == 0:
    print('O valor de cada parcela é R$ {}'.format(valorParcela))
    
    print('O valor total a pagar é R$ {}'.format(valorParcela*numParcelas))
else:
    residual = total - (parcela * numParcelas)
    print(residual)
    
    primeiraParcela = parcela + residual
    valorPrimeiraParcela = primeiraParcela / 100
    
    print('O valor da 1a parcela é R$ {}'.format(valorPrimeiraParcela))
    print('O valor das demais parcelas é R$ {}'.format(valorParcela))
    
    novoValorTotal = valorPrimeiraParcela + (numParcelas-1)*valorParcela
    print('O valor total a pagar é R$ {}'.format(novoValorTotal))
