import pandas as pd
from tabulate import tabulate
import os
import json

global dict_clientesBB
global dict_clientesNuBank
global dict_clientesItau
global dict_clientesUniversal

dict_clientesBB = {}
dict_clientesNuBank = {}
dict_clientesItau = {}

#Verificando a existência de registros
if os.path.exists('ProjetoBanco.json'):
    dict_clientesUniversal = {}
    with open ('ProjetoBanco.json','r') as f:
        dict_clientesUniversal = json.load(f)
else:
    dict_clientesUniversal = {'Banco do Brasil': dict_clientesBB, 'NuBank': dict_clientesNuBank, 'Itau': dict_clientesItau}


class Cliente():
    def __init__(self):
        self.dict_interno = None
        self.opcoes()

    def getBanco(self):
        if self.__askBanco == 'BB' or self.__askBanco == 'Banco do Brasil':
            return 'Banco do Brasil'
        elif self.__askBanco == 'It' or self.__askBanco == 'Itaú' or self.__askBanco == 'Itau':
            return 'Itau'
        elif self.__askBanco == 'Nu' or self.__askBanco == 'NuBank':
            return 'NuBank'
        else:
            return None

    def opcoes(self):
        # Opções gerais da classe Cliente
        print('\n+++++++++++ OPÇÕES +++++++++++\n')
        print('1 - Cadastrar cliente')
        print('2 - Consultar cliente')
        print('3 - Remover cliente')
        print('4 - Encerrar sessão')

        while True:
            op = input('\nDigite a opção desejada: ')
            if op == '1':
                self.Cadastro()
                break
            elif op == '2':
                self.ConsultarCliente()
                break
            elif op == '3':
                self.RemoverCliente()
                break
            elif op == '4':
                print('\nSessão encerrada.')
                break
            else:
                print('\nComando inválido.\n')

    def Cadastro(self):
        self.__askBanco = input('Banco (Banco do Brasil, NuBank, Itaú): ')
        cod = input('\nInforme o código do cliente: ')
        while True:
            try:
                if cod in dict_clientesUniversal[self.getBanco()].keys():
                    print('Código já cadastrado. Tente novamente ou digite E para Encerrar operação.')
                    cod = input('\nInforme o código do cliente: ')
                    if cod == 'E' or cod == 'e':
                        cnt = False
                        break
                else:
                    cnt = True
                    break
            except:
                print('Código inválido. Tente novamente ou digite E para Encerrar operação.')
                cod = input('\nInforme o código do cliente: ')
                if cod == 'E' or cod == 'e':
                    cnt = False
                    break

        if cnt == True:
            #Nesta etapa não foram feitos procedimentos de verificação dos dados
            nome = input('\nNome do cliente: ')
            tel = input('\nTelefone: ')
            cc = input('\nConta-corrente: ')
            cpf = input('\nCPF: ')
            nascimento = input('\nData de nascimento: ')
            senha = input('\nInforme uma senha: ')
            saldo = float(input('\nValor do primeiro depósito: '))

            dict_interno = {'nome': nome, 'cpf': cpf,'nascimento': nascimento, 'tel': tel, 'cc': cc, 'senha': senha, 'saldo':saldo}

            dict_clientesUniversal[self.getBanco()][cod] = dict_interno
            print('\nCliente cadastro com sucesso!\n')


        while True:
            print('\nRetornar ao menu de opções (R)')
            print('Encerrar sessão (E)')
            ask = input()
            if ask == 'r' or ask == 'R':
                self.opcoes()
                break
            elif ask == 'E' or ask == 'e':
                print('Encerrando sessão...')
                
                with open('ProjetoBanco.json','w') as f:
                    json.dump(dict_clientesUniversal,f)
                    break
                
                
            else:
                print('Comando inválido.\n')

    def ConsultarCliente(self):
        self.__askBanco = input('Banco (Banco do Brasil, NuBank, Itaú): ')
        cod = input('\nInforme o código do cliente: ')

        if cod in dict_clientesUniversal[self.getBanco()].keys():
            colunas = ['Nome', 'CPF', 'Data de nascimento', 'Telefone', 'Conta-corrente', 'Saldo']
            table = []
            infos = [dict_clientesUniversal[self.getBanco()][cod]['nome'], dict_clientesUniversal[self.getBanco()][cod]['cpf'], dict_clientesUniversal[self.getBanco()][cod]['nascimento'], dict_clientesUniversal[self.getBanco()][cod]['tel'], dict_clientesUniversal[self.getBanco()][cod]['cc'], dict_clientesUniversal[self.getBanco()][cod]['saldo']]
            table.append(infos)
            print(tabulate(table, headers=colunas, tablefmt='grid'))
        else:
            print(f'\nCliente de código {cod} não cadastrado no banco {self.getBanco()}.\n')
     
        while True:
            print('\nRetornar ao menu de opções (R)')
            print('Encerrar sessão (E)')
            ask = input()
            if ask == 'r' or ask == 'R':
                self.opcoes()
                break
            elif ask == 'E' or ask == 'e':
                print('Encerrando sessão...')
                
                with open('ProjetoBanco.json','w') as f:
                    json.dump(dict_clientesUniversal,f)
                    break
                
            else:
                print('Comando inválido.\n')

    def RemoverCliente(self):
        self.__askBanco = input('Banco (Banco do Brasil, NuBank, Itaú): ')
        cod = int(input('\nInforme o código do cliente: '))
        if cod in dict_clientesUniversal[self.getBanco()].keys():
            dict_clientesUniversal[self.getBanco()].pop(cod).values
            print(f'\nCliente de código {cod} removido do banco {self.getBanco()}.\n')
        else:
            print(f'\nCliente de código {cod} não cadastrado no banco {self.getBanco()}.\n')

        while True:
            print('\nRetornar ao menu de opções (R)')
            print('Encerrar sessão (E)')
            ask = input()
            if ask == 'r' or ask == 'R':
                self.opcoes()
                break
            elif ask == 'E' or ask == 'e':
                print('Encerrando sessão...')
                with open('ProjetoBanco.json','w') as f:
                    json.dump(dict_clientesUniversal,f)
                    break
                
            else:
                print('Comando inválido.\n')


class Login():
    def __init__(self):
        n = 0
        while True:
            self.__askBanco = input('\nBanco da conta: ')
            self.__cod = input('Código da conta: ')
            self.__askSenha = input('Senha da conta: ')
            if n <= 3:
                if self.getBanco() != None and self.getCod() in dict_clientesUniversal[self.getBanco()].keys() and self.getSenha() == dict_clientesUniversal[self.getBanco()][self.getCod()]['senha']:
                    print(f'Bem vindo(a) ao {self.getBanco()}')
                    break
                else:
                    print('\nDados não conferem! \nTente novamente.\n')
                    n += 1
            else:
                print('\nNúmero de tentativas excedidas. Conta temporariamente bloqueada.')
                break

    def getBanco(self):
        if self.__askBanco == 'BB' or self.__askBanco == 'Banco do Brasil':
            return 'Banco do Brasil'
        elif self.__askBanco == 'It' or self.__askBanco == 'Itaú' or self.__askBanco == 'Itau':
            return 'Itau'
        elif self.__askBanco == 'Nu' or self.__askBanco == 'NuBank':
            return 'NuBank'
        else:
            return None

    def getCod(self):
        return self.__cod

    def getSenha(self):
        return self.__askSenha

    def getNome(self):
        return dict_clientesUniversal[self.getBanco()][self.getCod()]['nome']

    def getCPF(self):
        return dict_clientesUniversal[self.getBanco()][self.getCod()]['cpf']

    def getNascimento(self):
        return dict_clientesUniversal[self.getBanco()][self.getCod()]['nascimento']

    def getCC(self):
        return dict_clientesUniversal[self.getBanco()][self.getCod()]['cc']

    def getSaldo(self):
        return dict_clientesUniversal[self.getBanco()][self.getCod()]['saldo']

    def getTel(self):
        return dict_clientesUniversal[self.getBanco()][self.getCod()]['tel']
        


class Banco(Login):
    def __init__(self):
        Login.__init__(self)
        self.__processos = []
        self.opcoes()

    def opcoes(self):
        print('\n+++++++++++ OPÇÕES +++++++++++\n')
        print('1 - Consultar saldo')
        print('2 - Depósito')
        print('3 - Saque')
        print('4 - Transferência')
        print('5 - Alterar dados pessoais')
        print('6 - Extrato')
        print('7 - Encerrar sessão')
        while True:
            op = input('\nDigite a opção desejada: ')

            if op == '1':
                self.consultarSaldo()
                break
            elif op == '2':
                self.deposito()
                break
            elif op == '3':
                self.saque()
                break
            elif op == '4':
                self.transferencia()
                break
            elif op == '5':
                self.dados()
                break
            elif op == '6':
                self.extrato()
                break
            elif op == '7':
                print('\nEncerrando sessão...')
                break
            else:
                print('\nComando inválido.\n')

    def consultarSaldo(self):
        Vsaldo = dict_clientesUniversal[self.getBanco()][self.getCod()]['saldo']
        print('--'*25)
        print(f'Saldo: R$ {Vsaldo}')
        print('--'*25)
        while True:
            print('\nRetornar ao menu de opções (R)')
            print('Encerrar sessão (E)')
            ask = input()
            if ask == 'r' or ask == 'R':
                self.opcoes()
                break
            elif ask == 'E' or ask == 'e':
                print('Encerrando sessão...')
                
                with open('ProjetoBanco.json','w') as f:
                    json.dump(dict_clientesUniversal,f)
                    break
                
            else:
                print('Comando inválido.\n')

    def deposito(self):
        valordep = input('Digite o valor do depósito: ')
        try:
            valordep = float(valordep)
            if valordep < 2:
                print('Valor mínimo para depósito: R$ 2,00. Operação não concluída.')
            else:
                dict_clientesUniversal[self.getBanco()][self.getCod()]['saldo'] = dict_clientesUniversal[self.getBanco()][self.getCod()]['saldo'] + valordep

                print('--'*25)
                print(f'R$ {valordep} reais adicionado à conta.\n')
                print('--'*25)
                self.__processos.append(f'Depósito no valor de R$ {valordep} reais.')
        # No caso de strings
        except:
            print('Valor inválido.')
        while True:
            print('\nRetornar ao menu de opções (R)')
            print('Encerrar sessão (E)')
            ask = input()
            if ask == 'r' or ask == 'R':
                self.opcoes()
                break
            elif ask == 'E' or 'e':
                print('Encerrando sessão...')
                
                with open('ProjetoBanco.json','w') as f:
                    json.dump(dict_clientesUniversal,f)
                    break

                
            else:
                print('Comando inválido.\n')
            

    def saque(self):
        valorsaq = input('Digite o valor do saque: ')
        try:
            valorsaq = float(valorsaq)
            if valorsaq > self.getSaldo():
                print('\nSaldo insuficiente.')
            else:
                dict_clientesUniversal[self.getBanco()][self.getCod()]['saldo'] = dict_clientesUniversal[self.getBanco()][self.getCod()]['saldo'] - valorsaq

                print('--'*25)
                print(f'R$ {valorsaq} reais retirados da conta.\n')
                print('--'*25)
                self.__processos.append(f'Saque no valor de R$ {valorsaq} reais.')
        #No caso de strings
        except:
            print('Valor inválido.')
        while True:
            print('Retornar ao menu de opções (R)')
            print('Encerrar sessão (E)')
            ask = input()
            if ask == 'r' or ask == 'R':
                self.opcoes()
                break
            elif ask == 'E' or 'e':
                print('Encerrando sessão...')
                
                with open('ProjetoBanco.json','w') as f:
                    json.dump(dict_clientesUniversal,f)
                    break

            else:
                print('Comando inválido.\n')

    def dados(self):
        ask = input('\nDigite o dado a ser alterado (Telefone/Senha): ')
        while True:
            if ask == 'Telefone' or ask == 'telefone' or ask == 'TELEFONE':
                self.alterarTelefone()
                break
            elif ask == 'Senha' or ask == 'senha' or ask == 'SENHA':
                self.alterarSenha()
                break
            elif ask == 'E' or ask == 'e':
                self.opcoes()
                break
            else:
                print('Comando inválido. Tente novamente ou digite E para encerrar a operação.')
                ask = input('\nDigite o dado a ser alterado (Telefone/Senha): ')


    def transferencia(self):
        codDestino = input('\nCódigo da conta de destino: ')

        #PRECISA VALIDAR O BANCO
        bancoDestino = input('Banco da conta de destino: ')
        # Verificando o banco
        bancos_validos = ['BB', 'Banco do Brasil', 'Nu', 'NuBank', 'It', 'Itaú', 'Itau']
        if bancoDestino not in bancos_validos:
            print('\nBanco inválido.\n')
        else:
            if bancoDestino == 'BB':
                bancoDestino = 'Banco do Brasil'
            elif bancoDestino == 'Nu':
                bancoDestino = 'NuBank'
            else:
                bancoDestino = 'Itau'

        valortransf = input('Valor da transferência: ')
        try:
            valortransf = float(valortransf)
            if valortransf > self.getSaldo():
                print('\nSaldo insuficiente.')
            else:
                if codDestino in dict_clientesUniversal[bancoDestino].keys():
                    #Conta de origem 
                    dict_clientesUniversal[self.getBanco()][self.getCod()]['saldo'] = dict_clientesUniversal[self.getBanco()][self.getCod()]['saldo'] - valortransf
                    #Conta de destino
                    destinatario = dict_clientesUniversal[bancoDestino][codDestino]['nome']
                    dict_clientesUniversal[bancoDestino][codDestino]['saldo'] = dict_clientesUniversal[bancoDestino][codDestino]['saldo'] + valortransf
                    print('--'*25)
                    print(f'Transferência no valor de R$ {valortransf} reais realizada para conta de {destinatario} do banco {bancoDestino}.')
                    print('--'*25)
                    self.__processos.append(f'Transferência no valor de R$ {valortransf} reais realizada para conta de {destinatario} do banco {bancoDestino}.')
                else:
                    print(f'\nA conta {codDestino} não existe no banco {bancoDestino}.')

        #No caso de strings
        except:
            print('Valor inválido.')
        while True:
            print('\nRetornar ao menu de opções (R)')
            print('Encerrar sessão (E)')
            ask = input()
            if ask == 'r' or ask == 'R':
                self.opcoes()
                break
            elif ask == 'E' or 'e':
                print('Encerrando sessão...')
                
                with open('ProjetoBanco.json','w') as f:
                    json.dump(dict_clientesUniversal,f)
                    break
                
            else:
                print('Comando inválido.\n')


    def alterarTelefone(self):
        print(f'\nTelefone atual: {self.getTel()}')
        ask2 = input('Novo telefone: ')
        dict_clientesUniversal[self.getBanco()][self.getCod()]['tel'] = ask2 
        print('--'*25)
        print('\nTelefone alterado com sucesso.\n')
        print('--'*25)         
        while True:
            print('Retornar ao menu de opções (R)')
            print('Encerrar sessão (E)')
            ask = input()
            if ask == 'r' or ask == 'R':
                self.opcoes()
                break
            elif ask == 'E' or ask == 'e':
                print('Encerrando sessão...')
                
                with open('ProjetoBanco.json','w') as f:
                    json.dump(dict_clientesUniversal,f)
                    break
                
            else: 
                print('Comando inválido.\n') 
            
    def alterarSenha(self):
        print(f'\n Senha atual: {self.getSenha()}')
        ask2 = input('Nova senha: ')
        dict_clientesUniversal[self.getBanco()][self.getCod]['senha'] = ask2 
        print('--'*25)
        print('\nSenha alterada com sucesso.\n')
        print('--'*25)         
        while True:
            print('Retornar ao menu de opções (R)')
            print('Encerrar sessão (E)')
            ask = input()
            if ask == 'r' or ask == 'R':
                self.opcoes()
                break
            elif ask == 'E' or ask == 'e':
                print('Encerrando sessão...')
                
                with open('ProjetoBanco.json','w') as f:
                    json.dump(dict_clientesUniversal,f)
                    break         
            else: 
                print('Comando inválido.\n') 
            
    def extrato(self):
        print('\n+++++++++++ EXTRATO +++++++++++\n')
        extratoUniversalCliente = dict_clientesUniversal[self.getBanco()][self.getCod()]['extrato']
        for i in range(len(extratoUniversalCliente)):
            print(extratoUniversalCliente[i])
            print('--'*25)
        while True:
            print('\n\n')
            print('Retornar ao menu de opções (R)')
            print('Encerrar sessão (E)')
            ask = input()
            if ask == 'r' or ask == 'R':
                self.opcoes()
                break
            elif ask == 'E' or ask == 'e':
                print('Encerrando sessão...')
                dict_clientesUniversal[self.getBanco()][self.getCod()]['extrato'] = self.__processos
                with open('ProjetoBanco.json','w') as f:
                    json.dump(dict_clientesUniversal,f)
                    break
    
            else: 
                print('Comando inválido.\n')

class Registro():
    def __init__(self):
        colunas = ['Código','Nome', 'CPF', 'Data de nascimento', 'Telefone', 'Conta-corrente', 'Saldo']

        if os.path.exists('ProjetoBanco.json'):
            with open ('ProjetoBanco.json','r') as f:
                dadosArquivados = json.load(f)
                
                for chave in dadosArquivados.keys():
                    print(f'\n{chave.upper()}')
                    linhas = []
                    for COD in dadosArquivados[chave].keys():
                        infos = [COD,dadosArquivados[chave][COD]['nome'], dadosArquivados[chave][COD]['cpf'],\
                                dadosArquivados[chave][COD]['nascimento'], dadosArquivados[chave][COD]['tel'],\
                                dadosArquivados[chave][COD]['cc'], dadosArquivados[chave][COD]['saldo']]
                        linhas.append(infos)
                    print(tabulate(linhas, headers = colunas,tablefmt="grid"))

        else:
            print('\nSem registros.\n')
