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
print("saiu")

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

print("\n---EXTRATO---")
print("Depósitos:")
for indice, depositos in enumerate(ex_deposito):
    print(f"{indice}: {depositos}")
print("Saques:")
for indice, saques in enumerate(ex_saque):
    print(f"{indice}: {saques}")
print(f"SALDO FINAL: R${deposito:.2f}")