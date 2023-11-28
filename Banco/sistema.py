import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication
from datetime import datetime
import os
from tela_menu import Tela_Menu
from tela_registrar import Tela_Registrar
from tela_sacar import Tela_Sacar
from tela_extrato import Tela_Extrato
from tela_depositar import Tela_Depositar
from tela_transferir import Tela_Transferir
from tela_login import Tela_Login
import random


class UiMain(QtWidgets.QWidget):

    def setupUi(self,Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.tela_login = Tela_Login()
        self.tela_login.setupUi( (self.stack0) )

        self.tela_registrar = Tela_Registrar()
        self.tela_registrar.setupUi( (self.stack1) )

        self.tela_menu = Tela_Menu()
        self.tela_menu.setupUi((self.stack2))

        self.tela_sacar = Tela_Sacar()
        self.tela_sacar.setupUi( (self.stack3) )

        self.tela_depositar = Tela_Depositar()
        self.tela_depositar.setupUi( (self.stack4) )

        self.tela_transferir = Tela_Transferir()
        self.tela_transferir.setupUi((self.stack5))

        self.tela_extrato = Tela_Extrato()
        self.tela_extrato.setupUi( (self.stack6) )

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)

class Main(QMainWindow, UiMain):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.nome = ""

        self.tela_login.pushButton_login.clicked.connect(self.botaoLogin)
        self.tela_login.pushButton_register.clicked.connect(self.TelaRegister)

        self.tela_registrar.pushButton_registrar.clicked.connect(self.botaoRegister)
        self.tela_registrar.pushButton_sair.clicked.connect(self.botaoVoltar)

        self.tela_menu.pushButton_depositar.clicked.connect( self.TelaDepositar )
        self.tela_menu.pushButton_sacar.clicked.connect( self.TelaSacar )
        self.tela_menu.pushButton_transferir.clicked.connect( self.TelaTransferir )
        self.tela_menu.pushButton_extrato.clicked.connect( self.TelaExtrato )
        self.tela_menu.pushButton_sair.clicked.connect( self.TelaSair )

        self.tela_sacar.pushButton_transferir.clicked.connect(self.botaoSacar)
        self.tela_sacar.pushButton_sair.clicked.connect( self.TelaMenu )

        self.tela_depositar.pushButton_Depositar.clicked.connect( self.botaoDepositar )
        self.tela_depositar.pushButton_sair.clicked.connect( self.TelaMenu )

        self.tela_transferir.pushButton_transferir.clicked.connect( self.botaoTransferir )
        self.tela_transferir.pushButton_sair.clicked.connect( self.TelaMenu )

        self.tela_extrato.pushButton_sair.clicked.connect( self.TelaMenu)

    def botaoLogin(self):
        senha = self.tela_login.lineEdit_password.text()
        name = self.tela_login.lineEdit_user.text()
        

        # Obtém o diretório atual do script
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))


        with open(os.path.join(diretorio_atual, 'dados', 'usuarios.txt'), 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()
        with open(os.path.join(diretorio_atual, 'dados', 'senhas.txt'), 'r') as arquivoUsuario:
            senhas = arquivoUsuario.readlines()

        usuarios = list( map( lambda x: x.replace( '\n', '' ), usuarios ) )

        senhas = list( map( lambda x: x.replace( '\n', '' ), senhas ) )

        logado = False

        for i in range( len( usuarios ) ):
            if name == usuarios[i] and senha == senhas[i]:
                QMessageBox.information( None, 'Mensagem', 'Usuario Logado!' )
                logado = True

                self.tela_login.lineEdit_user.setText( '' )
                self.tela_login.lineEdit_password.setText( '' )
                self.nome = name

                self.TelaMenu()

        if not logado:
            QMessageBox.information( None, 'Mensagem', 'Usuario ou senha incorreto!' )
            self.tela_login.lineEdit_user.setText( '' )
            self.tela_login.lineEdit_password.setText( '' )

    def botaoRegister(self):
        nome = self.tela_registrar.lineEdit_nome.text()
        cpf = self.tela_registrar.lineEdit_cpf.text()
        nascimento = self.tela_registrar.lineEdit_nascimento.text()
        senha = self.tela_registrar.lineEdit_password.text()
        numero = random.randint(100, 300)
        numero=str(numero)
        extrato = ('Data de Abertura: ' + str(datetime.today()))
        cadastro = False
        if not (nome == '' or senha == '' or cpf == '' or nascimento == ''):
             # verifica se login e senha ja n estao cadastrados
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))
            arquivo_cpf = os.path.join(diretorio_atual, 'dados', 'cpf.txt')
            if os.path.exists(arquivo_cpf):
                with open(os.path.join(diretorio_atual, 'dados', 'cpf.txt'), 'r') as arquivoUsuario:
                    cpfs = arquivoUsuario.readlines()

                cpfs = list( map( lambda x: x.replace( '\n', '' ), cpfs ) )
            
                # Verifica se ja existe o cadastro
                for i in range( len( cpfs ) ):
                    if cpf == cpfs[i]:
                        cadastro = True
                # Verifica se o numero da conta gerado ja existe e gera outro.
                diretorio_atual = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(diretorio_atual, 'dados', 'numero.txt'), 'r') as arquivoUsuario:
                    numeros_existentes = arquivoUsuario.readlines()

                numeros_existentes = list(map(lambda x: x.replace('\n', ''), numeros_existentes))

                # Verifica se o novo número já existe
                while novo_numero in numeros_existentes:
                    novo_numero = random.randint(1, 200)
                numero = str(novo_numero)

            # se os dados nao estiverem em branco
            if cadastro == False:
                # insere no arquivo
                diretorio_atual = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(diretorio_atual, 'dados', 'usuarios.txt'), 'a') as arquivoUsuario:
                    arquivoUsuario.write( nome + '\n' )

                diretorio_atual = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(diretorio_atual, 'dados', 'senhas.txt'), 'a') as arquivoUsuario:
                    arquivoUsuario.write( senha + '\n' )

                diretorio_atual = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(diretorio_atual, 'dados', 'cpf.txt'), 'a') as arquivoUsuario:
                    arquivoUsuario.write( cpf + '\n' )

                diretorio_atual = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(diretorio_atual, 'dados', 'nascimento.txt'), 'a') as arquivoUsuario:
                    arquivoUsuario.write( nascimento + '\n' )

                diretorio_atual = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(diretorio_atual, 'dados', 'numero.txt'), 'a') as arquivoUsuario:
                    arquivoUsuario.write( numero + '\n' )

                diretorio_atual = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(diretorio_atual, 'dados', 'saldo.txt'), 'a') as arquivoUsuario:
                    arquivoUsuario.write( '0.00' + '\n' )

                diretorio_atual = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(diretorio_atual, 'dados', 'extrato.txt'), 'a') as arquivoUsuario:
                    arquivoUsuario.write( extrato + '\n' )
                QMessageBox.information( None, 'REGISTER', 'Registrado com sucesso!' )
                self.tela_registrar.lineEdit_nome.setText( '' )
                self.tela_registrar.lineEdit_cpf.setText( '' )
                self.tela_registrar.lineEdit_nascimento.setText( '' )
                self.tela_registrar.lineEdit_password.setText( '' )
                
            else:
                self.tela_registrar.lineEdit_nome.setText( '' )
                self.tela_registrar.lineEdit_cpf.setText( '' )
                self.tela_registrar.lineEdit_nascimento.setText( '' )
                self.tela_registrar.lineEdit_password.setText( '' )
                QMessageBox.information( None, 'Mensagem', 'Login ou senha existentes!\nDigite novamente!' )
        else:
            QMessageBox.information( None, 'Mensagem', 'Todos os valores devem ser preenchidos!' )

    def botaoVoltar(self):
        self.tela_registrar.lineEdit_nome.setText( '' )
        self.tela_registrar.lineEdit_cpf.setText( '' )
        self.tela_registrar.lineEdit_nascimento.setText( '' )
        self.tela_registrar.lineEdit_password.setText( '' )
        self.QtStack.setCurrentIndex( 0 )

    def TelaRegister(self):
        self.QtStack.setCurrentIndex(1)

    def TelaSair(self):
        self.QtStack.setCurrentIndex( 0 )

    def TelaSacar(self):
        self.QtStack.setCurrentIndex( 3 )

    def TelaDepositar(self):
        self.QtStack.setCurrentIndex( 4 )

    def TelaTransferir(self):
        self.QtStack.setCurrentIndex(5)

    def TelaExtrato(self):
        self.QtStack.setCurrentIndex( 6 )

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'usuarios.txt'), 'r') as arquivoUsuario:
            usuario = arquivoUsuario.readlines()

        usuario = list( map( lambda x: x.replace( '\n', '' ), usuario ) )
        
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'extrato.txt'), 'r') as arquivoUsuario:
            extrato = arquivoUsuario.readlines()

        extrato = list( map( lambda x: x.replace( '\n', '' ), extrato ) )

        for i in range(len(extrato)):
            if self.nome == usuario[i]:
                ext = ''.join(extrato[i])
                self.tela_extrato.textBrowser.setText(ext)

    def TelaMenu(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'usuarios.txt'), 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()
        
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'numero.txt'), 'r') as arquivoUsuario:
            numeros = arquivoUsuario.readlines()

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'saldo.txt'), 'r') as arquivoUsuario:
            saldos = arquivoUsuario.readlines()
        
        usuarios = list( map( lambda x: x.replace( '\n', '' ), usuarios ) )

        numeros = list( map( lambda x: x.replace( '\n', '' ), numeros ) )

        saldos = list( map( lambda x: x.replace( '\n', '' ), saldos ) )

        for i in range( len( usuarios ) ):
            if self.nome == usuarios[i]:
                numero = numeros[i]
                saldo = saldos[i]

        self.QtStack.setCurrentIndex(2)
        self.tela_menu.lineEdit_cliente.setText(self.nome)
        self.tela_menu.lineEdit_numero.setText(numero)
        self.tela_menu.lineEdit_saldo.setText(saldo)
        
        self.tela_sacar.lineEdit_cliente.setText( self.nome )
        self.tela_sacar.lineEdit_numero.setText(numero)
        self.tela_sacar.Edit_saldo.setText(saldo)

        self.tela_depositar.lineEdit_cliente.setText( self.nome )
        self.tela_depositar.lineEdit_numero.setText( numero )
        self.tela_depositar.lineEdit_saldo.setText(saldo)
        
        self.tela_transferir.lineEdit_cliente.setText( self.nome )
        self.tela_transferir.lineEdit_numero.setText( numero )
        self.tela_transferir.lineEdit_saldo.setText(saldo)

    def botaoSacar(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'usuarios.txt'), 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'saldo.txt'), 'r') as arquivoUsuario:
            saldos = arquivoUsuario.readlines()

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'extrato.txt'), 'r') as arquivoUsuario:
            extrato = arquivoUsuario.readlines()


        usuarios = list( map( lambda x: x.replace( '\n', '' ), usuarios ) )

        saldos = list( map( lambda x: x.replace( '\n', '' ), saldos ) )

        extrato = list( map( lambda x: x.replace( '\n', '' ), extrato ) )

        valor = self.tela_sacar.lineEdit_saldo.text()
        if valor != '':
            valor = float(valor)
            Money = False
            for i in range( len( usuarios ) ):
                if self.nome == usuarios[i] and float(saldos[i]) - valor >= 0:
                    s = float( saldos[i] )
                    s = s - valor
                    saldos[i] = str(s)
                    Money = True
                    QMessageBox.information( None, 'Mensagem', 'Sacado com sucesso!' )
                    extrato[i] = (extrato[i] + '\t\t\tSaque realizado no valor de: {} reais'.format( valor ) )
                    

            if Money != True:
                QMessageBox.information( None, 'Mensagem', 'Saldo Insuficiente!' )
            """
            with open( 'saldo.txt', 'w' ) as arquivoUsuario:
                arquivoUsuario.write( '' )
            with open( 'extrato.txt', 'w' ) as arquivo:
                arquivo.write( '' )
            for j in range( len( usuarios ) ):
                with open( 'saldo.txt', 'a' ) as arquivoUsuario:
                    arquivoUsuario.write( saldos[j] + '\n' )
                with open( 'extrato.txt', 'a' ) as arquivo:
                    arquivo.write( extrato[j] + '\n' )
            """
            self.atualizar(usuarios,saldos,extrato)
        else:
            QMessageBox.information( None, 'Mensagem', 'Digite o valor!' )
        self.tela_sacar.lineEdit_saldo.setText( '' )

    

    def atualizar(self,usuarios,saldos,extrato):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'saldo.txt'), 'w') as arquivoUsuario:
            arquivoUsuario.write( '' )
        
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'extrato.txt'), 'w') as arquivoUsuario:
            arquivoUsuario.write( '' )
        for j in range( len( usuarios ) ):
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(diretorio_atual, 'dados', 'saldo.txt'), 'a') as arquivoUsuario:
                arquivoUsuario.write( saldos[j] + '\n' )
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(diretorio_atual, 'dados', 'extrato.txt'), 'a') as arquivoUsuario:
                arquivoUsuario.write( extrato[j] + '\n' )

    def botaoDepositar(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'usuarios.txt'), 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'saldo.txt'), 'r') as arquivoUsuario:
            saldos = arquivoUsuario.readlines()

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'extrato.txt'), 'r') as arquivoUsuario:
            extrato = arquivoUsuario.readlines()

        usuarios = list( map( lambda x: x.replace( '\n', '' ), usuarios ) )

        saldos = list( map( lambda x: x.replace( '\n', '' ), saldos ) )

        extrato = list( map( lambda x: x.replace( '\n', '' ), extrato ) )

        valor = self.tela_depositar.lineEdit_valor.text()
        if valor != '':
            valor = float( valor )
            for i in range( len( usuarios ) ):
                if self.nome == usuarios[i]:
                    s = float( saldos[i] )
                    s = s + valor
                    saldos[i] = str(s)
                    QMessageBox.information( None, 'Mensagem', 'Depositado com sucesso!' )
                    extrato[i] = (extrato[i] + '\t\t\tDeposito realizado no valor de: {}'.format(valor))

            self.atualizar(usuarios,saldos,extrato)

        else:
            QMessageBox.information( None, 'Mensagem', 'Digite o valor!' )
        self.tela_depositar.lineEdit_valor.setText( '' )

    def botaoTransferir(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'usuarios.txt'), 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'saldo.txt'), 'r') as arquivoUsuario:
            saldos = arquivoUsuario.readlines()

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'numero.txt'), 'r') as arquivoUsuario:
           numeros = arquivoUsuario.readlines()

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(diretorio_atual, 'dados', 'extrato.txt'), 'r') as arquivoUsuario:
            extrato = arquivoUsuario.readlines()

        usuarios = list( map( lambda x: x.replace( '\n', '' ), usuarios ) )

        saldos = list( map( lambda x: x.replace( '\n', '' ), saldos ) )

        numeros = list( map( lambda x: x.replace( '\n', '' ), numeros ) )

        extrato = list( map( lambda x: x.replace( '\n', '' ), extrato ) )

        num_destino = self.tela_transferir.lineEdit_numero_destino.text()
        valor = self.tela_transferir.lineEdit_transf_destino.text()

        if num_destino != '' and valor != '':
            valor = float(valor)
            Money = False

            for i in range( len( usuarios ) ):
                # Retira da conta
                if self.nome == usuarios[i] and float( saldos[i] ) - valor >= 0 and num_destino in numeros:
                    s = float( saldos[i] )
                    s = s - valor
                    saldos[i] = str( s )
                    Money = True
                    extrato[i] = (extrato[i] + '\t\t\tTranferencia realizado no valor de: {} para conta: {}'.format( valor,num_destino))


            if not num_destino in numeros:
                QMessageBox.information( None, 'Mensagem', 'Conta não existente!' )

                # Deposita na conta
            for i in range( len( numeros ) ):
                if num_destino == numeros[i] and Money == True:
                    s = float( saldos[i] )
                    s = s + valor
                    saldos[i] = str( s )
                    extrato[i] = (extrato[i] + '\t\t\tDeposito recebido no valor de: {}'.format( valor ))


                    QMessageBox.information( None, 'Mensagem', 'Transferido com sucesso!' )
            if Money != True and num_destino in numeros:
                QMessageBox.information( None, 'Mensagem', 'Saldo Insuficiente!' )

            self.atualizar( usuarios, saldos, extrato )

            self.tela_transferir.lineEdit_transf_destino.setText('')
            self.tela_transferir.lineEdit_numero_destino.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())