menu = '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
'''

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        valor_deposito = float(input('Informa o valor do depósito:'))
        if not valor_deposito > 0:
            print('Informe um valor válido para depositar')
            continue

        saldo += valor_deposito
        extrato.append('Depósito de '+str(valor_deposito))
        print('Depósito realizado com sucesso')
            
    if opcao == 's':
        valor_saque = float(input('Informa o valor para saque:'))
        
        if numero_saques == LIMITE_SAQUES:
            print('Você ultrapassou o limite de {} saques diários'.format(LIMITE_SAQUES))
            continue
        
        if not valor_saque > 0:
            print('Informe um valor para sacar')
            continue
        
        if valor_saque >= saldo:
            print('Você não possui saldo para sacar, consulte seu extrato')
            continue
        
        if not valor_saque <= limite:
            print('Você só pode sacar valores de até {} por operação'.format(limite))
            continue
            
        saldo -= valor_saque
        numero_saques += 1
        extrato.append('Saque de '+str(valor_saque))
        print('Saque realizado com sucesso')
        
    if opcao == 'e':
        for item in extrato:
            print(item)
        print('Saldo: {}'.format(saldo))
    
    if opcao == 'q':
        break