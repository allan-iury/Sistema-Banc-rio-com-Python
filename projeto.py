def depositar(saldo, historico_depositos):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        historico_depositos.append(f"Depósito: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, historico_depositos

def sacar(saldo, historico_saques, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        historico_saques.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, historico_saques, numero_saques

def exibir_extrato(saldo, historico_depositos, historico_saques):
    print("\n================ EXTRATO ================")

    if historico_depositos:
        print("---- HISTÓRICO DE DEPÓSITOS ----")
        print("\n".join(historico_depositos))
    else:
        print("Nenhum depósito foi realizado.")
    
    if historico_saques:
        print("\n---- HISTÓRICO DE SAQUES ----")
        print("\n".join(historico_saques))
    else:
        print("\nNenhum saque foi realizado.")

    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    historico_depositos = []
    historico_saques = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            saldo, historico_depositos = depositar(saldo, historico_depositos)
        elif opcao == "s":
            saldo, historico_saques, numero_saques = sacar(saldo, historico_saques, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, historico_depositos, historico_saques)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
