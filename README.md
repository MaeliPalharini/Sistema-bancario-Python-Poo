# 💰 Sistema Bancário em Python utilizando Programação Orientada a Objetos (POO)
Este projeto é uma implementação simples de um sistema bancário em Python, que inclui funcionalidades como criação de
contas, depósitos, saques, transferências e consulta de extratos. Utiliza conceitos de Programação Orientada a Objetos 
(POO) como herança, polimorfismo e classes abstratas.

## ✳️ Funcionalidades
- *Criar novos clientes*
- *Criar novas contas para os clientes*
- *Realizar depósitos em contas*
- *Realizar saques de contas*
- *Transferir dinheiro entre contas*
- *Listar todas as contas*
- *Exibir extrato de contas*
- *Registrar atividades com decorador de log*: Automatiza o registro de todas as operações bancárias, 
facilitando o monitoramento e a auditoria.
- *Gerar relatórios com geradores*: Permite a criação de relatórios dinâmicos que são construídos sob 
demanda, melhorando a eficiência da memória.
- *Iterar sobre contas com iterador personalizado*: Facilita a manipulação e acesso a contas através
de um iterador customizado que implementa comportamentos específicos.

## 🏗️Estrutura do Código

1. **Cliente🧑‍💼**:
   - Representa um cliente do banco.
   - Atributos: `endereco`, `contas`.
   - Métodos: `realizar_transacao`, `adicionar_conta`.

2. **PessoaFisica**:
   - Subclasse de `Cliente`.
   - Atributos: `nome`, `data_nascimento`, `cpf`.

### Classes Principais

3. **Conta**:
   - Classe base para contas bancárias.
   - Atributos: `saldo`, `numero`, `agencia`, `cliente`, `historico`.
   - Métodos: `sacar`, `depositar`.

4. **ContaCorrente**:
   - Subclasse de `Conta`.
   - Atributos: `limite`, `limite_saques`.
   - Métodos: `sacar`.

5. **Historico**:
   - Armazena o histórico de transações de uma conta.
   - Métodos: `adicionar_transacao`.

6. **Transacao (Abstract Class)**:
   - Classe abstrata para transações bancárias.
   - Propriedades: `valor`.
   - Métodos: `registrar`.

7. **Saque**:
   - Subclasse de `Transacao`.
   - Atributos: `valor`.
   - Métodos: `registrar`.

8. **Deposito**:
   - Subclasse de `Transacao`.
   - Atributos: `valor`.
   - Métodos: `registrar`.

## 🏗️ Implementações Técnicas

### Decorador de Log
- Implementado para registrar automaticamente informações relevantes cada vez que uma transação é realizada.

### Gerador de Relatórios
- Utiliza geradores Python para criar relatórios de transações, otimizando o uso de recursos e permitindo a manipulação de grandes volumes de dados de forma eficiente.

### Iterador Personalizado
- Facilita a navegação através das contas do cliente, permitindo operações como filtragem e agregação durante a iteração.

## Exemplo de Uso de Novas Funcionalidades

1. **Usando o Decorador de Log**:
   ```python
   @log_transacao
   def sacar(self, valor):
       # código para saque
   
2. **Gerando um Relatório de Transações**:
   ```python
   for transacao in gerar_relatorio(transacoes):
       print(transacao)
   
3. **Iterando com o Iterador Personalizado**:
   ```python
   for conta in ContaIterator(minhas_contas):
      print(conta)
   
### Funções Auxiliares

- `menu()`: Exibe o menu de opções para o usuário.
- `filtrar_cliente(cpf, clientes)`: Filtra e retorna um cliente baseado no CPF.
- `recuperar_conta_cliente(cliente)`: Recupera a conta de um cliente.
- `depositar(clientes)`: Realiza um depósito em uma conta.
- `sacar(clientes)`: Realiza um saque de uma conta.
- `exibir_extrato(clientes)`: Exibe o extrato de uma conta.
- `criar_cliente(clientes)`: Cria um novo cliente.
- `criar_conta(numero_conta, clientes, contas)`: Cria uma nova conta para um cliente.
- `listar_contas(contas)`: Lista todas as contas existentes.

## Exemplo de Uso

1. Crie um novo cliente:
   ```python
   criar_cliente(clientes)
   
2. Crie uma nova conta para o cliente:
    ```python
    criar_conta(numero_conta, clientes, contas)

3. Realize um depósito:
    ```python
    depositar(clientes)

4. Realize um saque:
    ```python
    sacar(clientes)

5. Exiba o extrato da conta:
    ```python
    exibir_extrato(clientes)
   
## 🛠️ Tecnologias Utilizadas

- Python 3.12
- Bibliotecas: `os`, `sys`, `datetime`

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE]para mais detalhes.

MIT License

Copyright (c) 2024 [Maeli Palharini]

## ✍️ Autora

- [Maeli Palharini](https://github.com/maelipalharini)