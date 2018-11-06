'''
Agenda de Contatos
Python 3.6
-
by R4MSOLO
'''
import os
import time

def registrar():
    nome     = input("\nNome.....: ")
    email    = input("\nEmail....: ")
    telefone = input("\nTelefone.: ")
    endereco = input("\nEndereco.: ")
   
    arq = open('agenda.txt', 'a+')
    texto = f'{nome} {email} {telefone} {endereco}\n'
    arq.writelines(texto)
    arq.close()
    print('[+]Contato registrado com sucesso!')
    time.sleep(0.5)
    os.system('clear')
    main()
 
def lista_Contato(): #lista ordenando por nomes na exibição
    print('=============================================')
    print('   Lista: (A-Z)')
    print('=============================================\n')
 
    contatos = []
 
    # Lendo do arquivo
    arq = open('agenda.txt', 'r')
    texto = arq.readlines()
    for linha in texto :
        contatos.append(linha)
    arq.close()
 
    # Ordenando
    contatos.sort()
