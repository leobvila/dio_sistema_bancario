def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    limite_saques = 3
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Valor inválido para saque.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==============================")

def menu():
    print("\n========== MENU ==========")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")
    return int(input("Escolha uma opção: "))

def main():
    saldo = 0
    limite = 500
    numero_saques = 0
    limite_saques = 3
    extrato = ""

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, limite_saques)
        elif opcao == 3:
            exibir_extrato(saldo, extrato)
        elif opcao == 4:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()