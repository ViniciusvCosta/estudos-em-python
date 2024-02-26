print('{:=^40}'.format(' TECTUDO '))
preco = float(input('Valor total das compras: R$'))

#opções de pagamento
print('''FORMAS DE PAGAMENTO
      [1] à vista no dinheiro/cheque
      [2] à vista no cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
opcao = int(input('Qual sera a forma de pagamento '))

#Calculo das opções
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = float(input('Quantas parcelas serão? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {:.0f}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preco
    print('OPÂO DE PAGAMENTO INVALIDA, tente novamente!')

#Saida final de dados
print('Sua compra de R${:.2f} vai ficar no valor de R${:.2f}'.format(preco, total))

print('{:=^40}'.format(' TECTUDO '))
