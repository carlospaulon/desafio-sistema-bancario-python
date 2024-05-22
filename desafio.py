print("Seja bem-vindo ao Sistema Bancário Python!")
menu = """
    ========== MENU ==========

    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Sair

    ========================== 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    try:
        opcao = int(input(menu))
        
        if opcao == 1:
            deposito = float(input("Informe o valor para depósito: "))
            if deposito > 0:
                saldo += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
            else: 
                print("Operação falhou! O valor informado é inválido!")

        elif opcao == 2:
            if numero_saques < 3:
                saque = float(input("Informe o valor para saque: "))
                
                excedeu_saldo = saque > saldo
                excedeu_limite = saque > limite

                if excedeu_saldo:
                    print("Operação falhou! Você não possui saldo suficiente.")

                elif excedeu_limite:
                    print("Operação falhou! O valor do saque excede o limite.")

                elif saque > 0:
                    saldo -= saque
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    numero_saques += 1

                else:
                    print("Operação falhou! O valor informado é inválido.")

            else:
                print("Operação falhou! Limite de saques diários excedidos!")

        elif opcao == 3:
            print(" Extrato ".center(38, "="))
            print(f"Não foram realizadas movimentações.\n{extrato}" if not extrato else extrato)
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            print("".center(38, "="))

        elif opcao == 4:
            print("Obrigado por utilizar o nosso Sistema Bancário! \nVolte sempre!!!")
            break
        
        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")
    except ValueError:
        print("Opção inválida! Por favor selecione novamente a operação desejada utilizando um valor númerico inteiro.")