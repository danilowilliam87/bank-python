# sistema bancário com as operações de: saque, depósito e extrato

banco = {}


def mostrar_menu():
    print("*************************** BEM VINDO BANCO SIRIGUEIJO**************************************")
    print("ESCOLHA A OPERAÇÃO QUE DESEJA REALIZAR:")
    print("[1] - SACAR")
    print("[2] - DEPOSITAR")
    print("[3] - EXTRATO")
    print("[4] - SAIR DA APLICAÇÃO")
    opcao = int(input("ESCOLHA UMA OPÇÃO:"))
    print("****************************************************************************")
    return opcao


def verificar_opcao_escolhida(opcao, nome):
    if opcao == 1:
        print("VOCE ESCOLHEU REALIZAR SAQUE:")
        valor_saque = float(input("INFORME O VALOR R$: "))
        sacar(nome, valor_saque)
    elif opcao == 2:
        print("VOCE ESCOLHEU REALIZAR UM DEPÓSITO:")
        valor_deposito = float(input("INFORME O VALOR R$: "))
        depositar(nome, valor_deposito)
    elif opcao == 3:
        print("VOCE ESCOLHEU MOSTRAR EXTRATO:")
        consultar_extrato(nome)
    elif opcao == 4:
        print("SAIR DO SISTEMA")
    else:
        print("OPÇÃO INVÁLIDA")


def criar_conta_corrente(nome, valor):
    print("$$$$$$$$$$$$$$$$$$$$$$$ CRIAR CONTA CORRENTE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    if not consultar_cliente(nome):
        if len(nome) > 0 and valor > 10:
            banco[nome] = valor
            print(f"CONTA CRIADA COM SUCESSO : {nome}. VALOR DEPOSITADO : {valor:,.2f}")
        else:
            print("IMPOSSÍVEL CRIAR CONTA, VERIFIQUE O NOME E/OU O VALOR DEPOSITADO")
    else:
        print(f"CLIENTE EXISTENTE -> TITULAR:{nome}. SALDO R$: {banco[nome]:,.2f}")

    print("$$$$$$$$$$$$$$$$$$$$$$$ FIM $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


def sacar(nome, valor):
    print("$$$$$$$$$$$$$$$$$$$$$$$ SAQUE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    if consultar_cliente(nome):
        saldo_conta = banco[nome]
        if saldo_conta < valor:
            print(f"IMPOSSÍVEL REALIZAR SAQUE. SALDO: R${banco[nome]:,.2f}")
        else:
            saldo_conta = saldo_conta - valor
            banco[nome] = saldo_conta
    else:
        print("CLIENTE INEXISTENTE")


def depositar(nome, valor):
    print("$$$$$$$$$$$$$$$$$$$$$$$ DEPÓSITO $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    if consultar_cliente(nome):
        saldo_conta = banco[nome]
        saldo_conta = saldo_conta + valor
        banco[nome] = saldo_conta
    else:
        print("CLIENTE INEXISTENTE")


def consultar_extrato(nome):
    print("$$$$$$$$$$$$$$$$$$$$$$$ EXTRATO BANCÁRIO $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    if consultar_cliente(nome):
        print("EXTRATO DA CONTA")
        print(f"TITULAR:{nome}")
        print(f"SALDO: R${banco[nome]:,.2f}")
        print("$$$$$$$$$$$$$$$$$$$$$$$ FIM $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


def consultar_cliente(nome):
    return nome in banco.keys()


def menu_novo_cliente(nome, valor):
    criar_conta_corrente(nome, valor)


if __name__ == '__main__':
    opt = 0
    titular = input("INFORME O TITULAR DA CONTA:")
    while opt != 4:
        if consultar_cliente(titular):
            opt = mostrar_menu()
            verificar_opcao_escolhida(opt, titular)
        else:
            resp = input("CLIENTE INEXISTENTE. DESEJA REALIZAR UM NOVO CADASTRO : [S]IM - [N]ÃO ? ")
            if resp == "S":
                saldo = float(input("INFORME O VALOR A SER DEPOSITADO R$: "))
                menu_novo_cliente(titular, saldo)
            else:
                print("$$$$$$$$$$$$$$$$$  FIM $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                opt = 4
