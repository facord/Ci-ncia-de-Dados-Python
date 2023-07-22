menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

deposito = 0
saque = 0
saque_limite = 0
while True:
    opcao = input(menu)
    if opcao == "d":
        print("Depósito")
        deposito = int(input("Informe o valor do depósito: "))
        ex_deposito = []
        ex_deposito.append(deposito)
        deposito1=1
        while (deposito1>0):
            deposito1 = int(input("Informe o valor do depósito: (Obs: 0 para Sair)"))
            if deposito1>0:
                deposito += deposito1
                ex_deposito.append(deposito1)
                print(deposito)
        continue
    elif opcao == "s":
        if saque_limite == 0: 
            print("Saque")
            ex_saque = []
            for i in range(0, 3):
                saque = int(input("Informe o valor do saque: R$"))
                if saque>500: 
                    print("Valor de saque inválido!")
                elif deposito<500: 
                    print(f"Seu saldo é menor que o valor do saque. R${deposito:.2f}")
                    break
                else: deposito -= saque; ex_saque.append(saque)
                print(f"Seu saldo é R${deposito:.2f}") 
                saque_limite = 1
        else: print("Atingiu o limite diário de saque!")
        continue 
    elif opcao == "e":
        print("\n---EXTRATO---")
        print("Depósitos:")
        for indice, depositos in enumerate(ex_deposito):
            print(f"{indice}: {depositos}")
        print("Saques:")
        for indice, saques in enumerate(ex_saque):
            print(f"{indice}: {saques}")
        print(f"SALDO FINAL: R${deposito:.2f}")
        continue
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        continue
