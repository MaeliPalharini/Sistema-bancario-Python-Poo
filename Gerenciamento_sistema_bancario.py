import textwrap


def menu() -> str:
    menu_text = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [t] Transferir
    [q] Sair
    => """
    return input(textwrap.dedent(menu_text))


def depositar(contas):
    numero_conta = input("Informe o número da conta para depósito: ")
    valor = float(input("Informe o valor do depósito: "))
    conta = next((conta for conta in contas if str(conta['numero_conta']) == numero_conta), None)
    if conta is None:
        print("\n@@@ Conta não encontrada! @@@")
        return

    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")


def sacar(contas):
    numero_conta = input("Informe o número da conta para saque: ")
    valor = float(input("Informe o valor do saque: "))
    conta = next((conta for conta in contas if str(conta['numero_conta']) == numero_conta), None)
    if conta is None or valor > conta['saldo']:
        print("\n@@@ Saldo insuficiente ou conta não encontrada. @@@")
        return
    conta['saldo'] -= valor
    conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
    print("\n=== Saque realizado com sucesso! ===")


def exibir_extrato(contas):
    numero_conta = input("Informe o número da conta para ver o extrato: ")
    conta = next((conta for conta in contas if str(conta['numero_conta']) == numero_conta), None)
    if conta:
        print("\n================ EXTRATO ================")
        print(conta['extrato'] if conta['extrato'] else "Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {conta['saldo']:.2f}\n==========================================")
    else:
        print("\n@@@ Conta não encontrada! @@@")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n=== Usuário criado com sucesso! ===")


def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    if not usuario:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return
    numero_conta = len(contas) + 1  # Incrementa o número da conta automaticamente
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "saldo": 0.0, "extrato": "", "usuario": usuario})
    print(f"\n=== Conta criada com sucesso! Número da conta: {numero_conta} ===")


def listar_contas(contas):
    if not contas:
        print("\nNão há contas registradas.")
        return
    print("\nListagem de contas:")
    for conta in contas:
        print(
            f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}, Saldo"
            f": R$ {conta['saldo']:.2f}")


def transferir(contas):
    de_num = input("Informe o número da conta de origem: ")
    para_num = input("Informe o número da conta de destino: ")
    valor = float(input("Informe o valor da transferência: "))
    de_conta = next((conta for conta in contas if conta['numero_conta'] == int(de_num)), None)
    para_conta = next((conta for conta in contas if conta['numero_conta'] == int(para_num)), None)
    if not de_conta or not para_conta or valor > de_conta['saldo']:
        print("\n@@@ Operação falhou! Verifique os dados ou saldo insuficiente. @@@")
        return
    de_conta['saldo'] -= valor
    de_conta['extrato'] += f"Transferência enviada: R$ {valor:.2f}\n"
    para_conta['saldo'] += valor
    para_conta['extrato'] += f"Transferência recebida: R$ {valor:.2f}\n"
    print("\n=== Transferência realizada com sucesso! ===")


def main():
    agencia = "0001"
    contas = []
    usuarios = []

    while True:
        opcao = menu()
        if opcao == "d":
            depositar(contas)
        elif opcao == "s":
            sacar(contas)
        elif opcao == "e":
            exibir_extrato(contas)
        elif opcao == "nc":
            criar_conta(agencia, contas, usuarios)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "t":
            transferir(contas)
        elif opcao == "q":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")


main()
