Este repositório é voltado ao armazenamento dos arquivos do Projeto Banco, realizado para disciplina
de Programação II do Bacharelado Interdisciplinar em Ciência e Tecnologia da Ufopa.

Organização: Yana S. Pereira (BICT 2020)

- Bibliotecas utilizadas:
    I. pandas;
    II. tabulate;
    III. os;
    IV. json.

- Variáveis globais:
    Fora criados dicionários para cada banco (Banco do Brasil, Itaú e NuBank). 
    Os dicionários de cada banco possui como chaves os códigos dos clientes e como valores dicionários internos que apresentam os dados dos clientes, no formato: 
    dicionarioBanco1 = {código: {'nome':nome, 'cpf':cpf...}}.
    Além disso, foi criado um dicionário que abarca os três dicionários dos bancos, no formato:
    dicionarioUniversal = {dicionarioBanco1:{}, dicionarioBanco2:{}, dicionarioBanco3:{}}.

    Um detalhe importante é os dados dos clientes são armazenados no arquivo externo "ProjetoBanco.json". Caso o arquivo já exista com dados já
    registrados, o dicionário universal carrega estes dados novamente. Se não, o arquivo é criado e o dicionário universal inicialmente é vazio.


- Arquivo classesBancarias.py  

    1. Classe Cliente():
        Possui uma função para retornar o banco do usuário e uma função para imprimir as operações (outras funções), que são:

            1.1. getBanco(self):
                Retorna o banco dado pelo usuário, validando a resposta e retornando None caso o banco dado seja inválido.

            1.2. opcoes(self):
                Imprime as possíveis operações da classe: a) cadastro de cliente; b) consulta de cliente; c) remoção de cliente.

            1.3. Cadastro():
                A função tem como objetivo cadastrar o cliente em um dos bancos possíveis (Banco do Brasil, Itaú, NuBank). Cada banco possui um dicionário cujas chaves são os códigos dos clientes, no formato:
                dicionarioBanco1 = {codigo: {'nome': nome, 'cpf': cpf...}}.
                Além disso, existe um dicionário universal que abarca os dicionários dos três bancos, no formato:
                dicionarioUniversal = {dicionarioBanco1:{}, dicionarioBanco2:{}, dicionarioBanco3:{}}.

            1.4. ConsultarCliente(self):
                Procura o registro do cliente no dicionário universal e imprime os dados do cliente em formato tabelado.

            1.5. RemoverCliente(self):
                Remove o cliente do dicionário universal.

    2. Classe Login():
        A inicialização da classe verifica se os dados apresentados pelo usuário coincidem com os registrados no seu cadastro, com 
        apenas 3 tentativas de sucesso.

            2.1. getBanco(self):
                Retorna o banco dado pelo usuário, validando a resposta e retornando None caso o banco dado seja inválido.
            
            2.2. getCod(self):
                Retorna o código do cliente dado pelo usuário.

            2.3. getSenha(self):
                Retorna a senha do cliente dada pelo usuário.

            2.4. getNome(self):
                Retorna o nome do usuário verificando seu registro no dicionário universal.
            
            2.5. getCPF(self):
                Retorna o CPF do usuário verificando seu registro no dicionário universal.

            2.6. getNascimento(self):
                Retorna a data de nascimento do usuário verificando seu registro no dicionário universal.
                Obs: pode-se criar uma função de verificação para que apenas maiores de idade possam criar contas nos bancos.

            2.7. getCC(self):
                Retorna a conta-corrente do usuário verificando seu registro no dicionário universal.

            2.8. getSaldo(self):
                Retorna o saldo do usuário verificando seu registro no dicionário universal.

            2.9. getTel(self):
                Retorna o telefone do usuário verificando seu registro no dicionário universal.

    3. Classe Banco(Login):
        Utiliza a inicialização da classe Login() para verificar autenticidade dos dados apresentados.
        O dicionário self.__processos é utilizado para armazenar as movimentações financeiras a serem adicionadas ao extrato.

            3.1. opcoes(self):
                Apresenta as operações possíveis da classe: a) Consultar Saldo; b) Depósito; c) Saque; d) Transferência; e) Alterar dados pessoais;
                f) Extrato; g) Encerrar.

            3.2. consultarSaldo(self):
                Retorna o saldo do usuário verificando o dicionário universal.

            3.3. deposito(self):
                Verifica o saldo atual e soma o valor do depósito, atualizando o valor do saldo no dicionário universal.

            3.4. saque(self):
                Verifica o saldo atual e subtrai o valor do saque, atualizando o valor do saldo no dicionário universal, caso o valor do saque
                não seja maior que o saldo em conta.

            3.5. dados(self):
                Verifica qual dado o usuário deseja alterar, o seu número de telefone ou a sua senha. 

            3.6. transferencia(self):
                Verifica o valor da transferência, bem como as informações da conta de destino.
                Subtrai o valor transferido do saldo do remetente e adiciona o valor transferido ao saldo do destinatário, no dicionário universal.

            3.7. alterarTelefone(self):
                É chamada pela função dados(self) e altera o telefone do usuário no dicionário universal.

            3.8. alterarSenha(self):
                É chamada pela função dados(self) e altera a senha do usuário no dicionário universal. 

            3.9. extrato(self):
                Imprime as movimentações financeiras feitas pelo cliente.


    4. Classe Registro():
            Imprime os dados dos clientes cadastrados em formato de tabela.     