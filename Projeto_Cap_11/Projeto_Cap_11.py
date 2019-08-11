"""

Projeto_Cap_11 - Crie um programa que aceite um endereço de email e uma string de texto na
linha de comando e então, faça login em sua conta de
email e envie um email contendo a string para o endereço fornecido. (Você
poderá criar uma conta separada de email para esse programa.)
Essa seria uma maneira interessante de acrescentar uma funcionalidade de
notificação em seus programas.

Created on Sat May 19 21:34:38 2018
@author: Edson Frota

"""
import smtplib # módulo define um objeto de sessão do cliente SMTP que pode ser usado para enviar mensagens para qualquer máquina da Internet
import getpass # Utilitários para obter uma senha e / ou o nome do usuário atual.

#Dados do Remetente
remetente = input("Digite seu email: ")
senha = getpass.getpass("Informe sua senha: ")

#Dados do Destinatário
destinatario = input("Digite o email do destinatario: ")
assunto = input("Informe o assunto do email: ")

#Mensagem
print('Escreva sua mensagem')
texto = input(" ")

#O termo join Junta cada item da string com um delimitador especificado.
mensagem = '\r\n'.join(['From: %s' % remetente, 'To: %s' % destinatario, 'Subject:%s' %assunto,'','%s' % texto])

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls() # Coloca a conexão com o servidor SMTP no modo TLS.
server.login(remetente,senha)
server.sendmail(remetente, destinatario, mensagem)
server.quit() # Encerre a sessão SMTP.