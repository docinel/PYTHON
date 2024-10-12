from abc import ABC, abstractmethod
from datetime import datetime
import textwrap


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def relizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._historico = Historico()
        self._agencia = '0001'
        self._cliente = cliente

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def saldo(self):
        return self._saldo

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('Saldo insuficiente')
            return False
        elif valor > 0:
            self._saldo -= valor
            return True
        else:
            print('Valor inválido')
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Operação realizada com sucesso')
        else:
            print('Valor inválido')
            return False


class ContaCorrente(conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self._historico.transacoes
             if transacao['tipo'] == Saque.__name__])

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques
        excedeu_saldo = not self.saldo >= valor

        if excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')
        elif excedeu_saques:
            print('Operação falhou! Número de saques excedido.')
        elif excedeu_saldo:
            print('Operação falhou! Saldo insuficiente.')
        else:
            super().sacar(valor)
            return False

    def __str__(self):
        return f'Número da conta: {self._numero} \nAgência: {self._agencia} \nSaldo: {self._saldo} \nTitular: {self._cliente.nome}'


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                'data': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
                'valor': transacao.valor,
                'tipo': transacao.__class__.__name__
            }
        )


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

    @property
    @abstractmethod
    def valor(self):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self._valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(Saque(self._valor))


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self._valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(Deposito(self._valor))


def menu():
    menu = """\n
    ===================MENU===================
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc] \tNova conta
    [lc] \tListar contas
    [nu] \tNovo usuário
    [q] \tSair
    ==> """
    return input(textwrap.dedent(menu))


def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes
                          if cliente.cpf == cpf]
    return clientes_filtrados[0] if len(clientes_filtrados) == 1 else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('Cliente não possui contas')
        return
    # FIXME: Acho que aqui tem um erro
    return cliente.contas[0]


def sacar(clientes):
    cpf = input('Qual o CPF do cliente? ')
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print('CPF não encontrado')
        return

    valor = float(input('Quanto deseja sacar? '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.relizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input('Qual o CPF do cliente? ')
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print('CPF não encontrado')
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    print('Extrato')
    print('--------')
    print(f'Saldo: {conta.saldo}')
    print('Transações:')
    for transacao in conta.historico.transacoes:
        print(f'{transacao["data"]} - {transacao["valor"]} - {transacao["tipo"]}')


def depositar(clientes):
    cpf = input('Qual o CPF do cliente? ')
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print('CPF não encontrado')
        return

    valor = float(input('Quanto deseja depositar? '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.relizar_transacao(conta, transacao)


def criar_cliente(clientes):
    cpf = input('Digite o CPF: ')
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print('Já existe um cliente com esse CPF.')
        return

    nome = input('Digite o nome: ')
    data_nascimento = input('Digite a data de nascimento: ')
    endereco = input('Digite o endereço: ')

    cliente = PessoaFisica(nome, endereco, data_nascimento, cpf)
    clientes.append(cliente)

    print('Cliente criado com sucesso!')


def criar_conta(clientes, contas, numero_conta):
    cpf = input('Qual o CPF do cliente? ')
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print('CPF não encontrado')
        return

    conta = ContaCorrente(cliente, numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print('Conta criada com sucesso!')


def listar_contas(contas):
    if not contas:
        print('Nenhuma conta encontrada.')
        return

    print('Contas:')
    for conta in contas:
        print(conta)


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            depositar(clientes)

        elif opcao == 's':
            sacar(clientes)

        elif opcao == 'e':
            exibir_extrato(clientes)

        elif opcao == 'nu':
            criar_cliente(clientes)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(clientes, contas, numero_conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break


main()
