total = totMil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome de produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totMil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.fomart('Fim do Programa'))
print('O total da compra foi R${:.2f}'.format(total))
print('Temos {} produtos custando mais de R$1000.00'.format(totMil))
print('O produto mais barato foi {} que custa R${:.2f}'.format(barato, menor))