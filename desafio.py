menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falou! O valor informado é invalido.")
    
    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = "Você não tem saldo suficiente. " if valor > saldo else False
        excedeu_limite = "O valor do saque excede o limite. " if valor > limite else False
        excedeu_saques = "Número máximo de saques excedido. " if numero_saques >= LIMITE_SAQUES else False

        if excedeu_saldo or excedeu_limite or excedeu_saques:
            mensagem = "Operação falhou! Confira a causa abaixo:\n"
            mensagem += excedeu_saldo if excedeu_saldo else ""
            mensagem += excedeu_limite if excedeu_limite else ""
            mensagem += excedeu_saques if excedeu_saques else ""
            
            print(mensagem)

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falou! O valor informado é invalido.")
    
    elif opcao == 3:
        print("\n============== EXTRATO ==============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=====================================")
    
    elif opcao == 4:
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")