#!/usr/bin/env python 
# -*- coding:utf-8 -*- 

import socket #Importando socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Definindo o tipo de socket que vamos utilizar 
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind(('', 7000)) #Passando o nome do host (uma string vazia já que qual quer um pode se conectar) e a porta de conexão 
s.listen(5) #Colocando em modo de escuta 
print ('aguardando conexao') 
con, server = s.accept() #Conexão aceita 
print ('conectado') 

recebe = con.recv(512) #Recebendo mensagem 
print(recebe) 

while True: #Looping infinito para poder enviar vários comandos 

    try: 

        cmd = raw_input('Digite um comando: ') #Comando a ser enviado 
        con.send(cmd) #Enviando comando 

        if cmd == 'quit': #Se o comando for quit fecha a conexão e sai do looping 
            s.close() 
            break 
        else: #Se não esera ser retornado uma mensagem 
            recebe = con.recv(512) 
            print(recebe) 

    except: #Caso de erro feche a conexão e saia do looping 
        s.close() 
        break  