import textwrap


def menu():
    menu = """\n
=============== MENU ===============
[d] \tDepositar
[s] \tSacar
[e] \tExtrato
[nc] \tNova conta
[lc] \tListar contas
[nu] \tNovo usuário
[q] \tSair
=> """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n*** Depósito realizado com sucesso! ***")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato


def sacar(*, saldo, valor, limite, extrato, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:

        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:

        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:

        print("\n@@@ Operação falhou! Número de saques excedido. @@@")

    elif valor > 0:

        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n*** Saque realizado com sucesso! ***")

    else:

        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("========== FINAL ==========")
    print("\n")


def criar_conta(usuarios, contas):
    print("Criando uma conta.")

    cpf = input("Qual o CPF do cliente? ")
    if cpf in usuarios:
        print("Já existe usuário com este CPF.")
        return
    else:
        print("Usuário criado com sucesso!")

    nome = input("Qual o nome do cliente? ")
    cpf = input("Qual o CPF do cliente? ")
    email = input("Qual o e-mail do cliente? ")

    conta = [nome, cpf, email]
    contas.append(conta)

    print("Conta criada com sucesso!")


def listar_contas(contas):
    for conta in contas:
        print("========== CONTA ==========")
        print(f"Nome: {conta[0]}")
        print(f"CPF: {conta[1]}")
        print(f"E-mail: {conta[2]}")
        print("===========================")


def novo_usuario(usuarios):
    print("Criando um novo usuário.")

    nome = input("Qual o nome do cliente? ")
    email = input("Qual o e-mail do cliente? ")
    cpf = input("Qual o CPF do cliente? ")

    usuarios.append([nome, email, cpf])

    print("Novo usuário criado com sucesso!")


def novo_saque(*, saldo, valor, limite, extrato, numero_saques, LIMITE_SAQUES):
    if valor > 0:
        if valor <= limite - saldo:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif numero_saques >= LIMITE_SAQUES:
            print("\n@@@ Operação falhou! Número de saques excedido. @@@")

        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n*** Saque realizado com sucesso! ***")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    LIMITE_DEPOSITO = 500
    LIMITE_SALDO = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Quanto deseja depositar? "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Quanto deseja sacar? "))
            saldo, extrato = sacar(saldo=saldo,
                                   valor=valor,
                                   limite=limite,
                                   extrato=extrato,
                                   numero_saques=numero_saques,
                                   LIMITE_SAQUES=LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nc":
            criar_conta(usuarios, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "nu":
            novo_usuario(usuarios)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor tente novamente.\n")

    print("Obrigado por utilizar nosso sistema bancário!")

    return 0


main()