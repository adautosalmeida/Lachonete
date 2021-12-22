def cardapio():
    print('|===============================================================================|')
    print('|                                LANCHONETE                                     |')
    print('|===============================================================================|')
    print('|     ITEM     |     PRODUTO          |     CÓDIGO     |     PREÇO UNITÀRIO     |')
    print('|===============================================================================|')
    print('|       1      |  CACHORRO-QUENTE     |      100       |          5.00          |')
    print('|       2      |    X-SALADA          |      101       |          8.79          |')
    print('|       3      |    X-BACON           |      102       |          9.99          |')
    print('|       4      |     MISTO            |      103       |          6.89          |')
    print('|       5      |     SALADA           |      104       |          4.80          |')
    print('|       6      |     AGUA             |      105       |          3.49          |')
    print('|       7      |  REFRIGERANTE        |      106       |          4.99          |')
    print('|===============================================================================|')
cardapio()  # exibe p menu para a escolha
preco_total = 0   # armazena o valor total da compra e vai sendo incrementado a cada escolha
                 # e apresenta o valor final da comando apos o programa ser encerrado
print(' >>>>> PARA REALIZAR SEU PEDIDO SELECIONE UM ITEM <<<<< ')
print(' >>>>> PARA FINALIZAR DIGITE [0] <<<<< ')
while True:

    try:
        print()
        print('>>>>> Entre com um Item <<<<< ')
        item = int(input('ITEM: '))
        

        if item == 1:
            print('PRODUTO: CACHORRO-QUENTE     VALOR UNITÁRIO: 5.00 ')
            quantidade = int(input('Informe a quantidade:  '))
            preco_total = preco_total + (quantidade * 5.00)
            print(f'PRODUTO: CACHORRO-QUENTE     QUANTIDADE: {quantidade}     VALOR TOTAL: {preco_total:.2f}')
        elif item == 2:
            print('PRODUTO: X-SALADA     VALOR UNITÁRIO: 8.79 ')
            quantidade = int(input('Informe a quantidade:  '))
            preco_total = preco_total + (quantidade * 8.79)
            print(f'PRODUTO: X-SALADA     QUANTIDADE: {quantidade}     VALOR TOTAL: {preco_total:.2f}')
        elif item == 3:
            print('PRODUTO: X-BACON     VALOR UNITÁRIO: 9.99 ')
            quantidade = int(input('Informe a quantidade:  '))
            preco_total = preco_total + (quantidade * 9.99)
            print(f'PRODUTO: X-BACON     QUANTIDADE: {quantidade}     VALOR TOTAL: {preco_total:.2f}')
        elif item == 4:
            print('PRODUTO: MISTO     VALOR UNITÁRIO: 6.89 ')
            quantidade = int(input('Informe a quantidade:  '))
            preco_total = preco_total + (quantidade * 6.89)
            print(f'PRODUTO: MISTO     QUANTIDADE: {quantidade}     VALOR TOTAL: {preco_total:.2f}')
        elif item == 5:
            print('PRODUTO: SALADA     VALOR UNITÁRIO: 4.80 ')
            quantidade = int(input('Informe a quantidade:  '))
            preco_total = preco_total + (quantidade * 4.80)
            print(f'PRODUTO: SALADA     QUANTIDADE: {quantidade}     VALOR TOTAL: {preco_total:.2f}')
        elif item == 6:
            print('PRODUTO: AGUA     VALOR UNITÁRIO: 3.49 ')
            quantidade = int(input('Informe a quantidade:  '))
            preco_total = preco_total + (quantidade * 3.49)
            print(f'PRODUTO: ÁGUA     QUANTIDADE: {quantidade}     VALOR TOTAL: {preco_total:.2f}')
        elif item == 7:
            print('PRODUTO: REFRIGERANTE     VALOR UNITÁRIO: 4.99 ')
            quantidade = int(input('Informe a quantidade:  '))
            preco_total = preco_total + (quantidade * 4.99)
            print(f'PRODUTO: REFRIGERANTE     QUANTIDADE: {quantidade}     VALOR TOTAL: {preco_total:.2f}')
        else:
            if item == 0:
                break
            elif item < 0 or item > 7:
                print('>>>>> Item Inválido <<<<<')
                print('>>>>> Tente Novamente <<<<<')
    except ValueError as error:
        print('>>>>> Entre com um valor valido <<<<< ')
        print('>>>>> O valor deve estar em conformidade com o MENU... <<<<<')

print(f'>>>>> O VALOR TOTAL DE SUA COMPRA FOI DE {preco_total:.2f} REAIS. <<<<<')
print()
print('>>>>> OBRIGADO E VOLTE SEMPRE <<<<<')

