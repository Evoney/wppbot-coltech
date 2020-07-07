from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotVisibleException

from urllib3.exceptions import ConnectionError

from wppbot import wppbot
from classes.cliente import Cliente
from classes.time import Data


import datetime
import time
from datetime import date


try:
    bot = wppbot()
    bot.inicia()
except (WebDriverException, ConnectionError, ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError, TimeoutException) as Error:
    print(Error)


global Clientes, ClientesEsperando
Clientes = []
ClientesEsperando = []


def atualiza_listas_clientes(lst1, lst2, cliente_buscado):
    Data_ = Data()

    if (len(lst2) > 0 and cliente_buscado != None):
        if (cliente_buscado.estado == 0):
            if (Data_.hora >= cliente_buscado.hora_inicio_atendimento + 1 and cliente_buscado.dia_inicio_atendimento == Data_.dia and cliente_buscado.mes_inicio_atendimento == Data_.mes):
                lst1.remove(cliente_buscado)
                lst2.remove(cliente_buscado)


def recupera_cliente_id(lst, id):
    cliente = None
    if (len(lst) > 0):
        for c in lst:
            if (c.id == id):
                cliente = c
    return cliente


def getTimePass(last_message, type):
    Data_ = Data()
    try:
        div_horario = last_message.find_element_by_class_name("copyable-text")
        data_mensagem = str(div_horario.get_attribute('data-pre-plain-text'))
        encontrou_data = True
    except (NoSuchElementException, NoSuchAttributeException, AttributeError) as Error:
        print(Error)

    if(encontrou_data == True):
        hora_mensagem = int(data_mensagem[1:3])
        minuto_mensagem = int(data_mensagem[4:6])
        dia_mensagem = int(data_mensagem[8:10])
        mes_mensagem = int(data_mensagem[11:13])

        if(type == 'client'):   
            if (Data_.dia == dia_mensagem and Data_.mes == mes_mensagem and Data_.hora == hora_mensagem and Data_.minuto <= minuto_mensagem + 20):
                return  True
            elif ( Data_.dia == dia_mensagem and Data_.mes == mes_mensagem and Data_.hora == hora_mensagem + 1):
                diferenca = 60 - minuto_mensagem
                if (diferenca + Data_.minuto < 20):
                    return True


        elif(type == 'bot'):                  
            if(Data_.dia == dia_mensagem and Data_.mes == mes_mensagem):
                return False
            else:
                return True
            


try:
    while True:
    
        bot.driver.implicitly_wait(600)
        div_contatos = bot.driver.find_element_by_class_name("_1qDvT")
        contatos = div_contatos.find_elements_by_class_name("_210SC")
        num_contatos = len(contatos)
        i = 0
        while i < num_contatos:
            contato = contatos[i]
            try:
                contato.click()
                clicou = True
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException, WebDriverException) as error:
                clicou = False

            if (clicou == True):
    
                time.sleep(2)

                mensagens = bot.driver.find_elements_by_class_name("_2hqOq")
                num_mensagens = len(mensagens)
                
                mensagens_bot = []
                j = 0

                while (j < num_mensagens):
                    
                    mensagem = mensagens[j]
                    classe_mensagem = mensagem.get_attribute('className')
                    if ('message-out' in classe_mensagem):
                        mensagens_bot.append(mensagem)
                    j += 1

              
                ultima_mensagem = mensagens[num_mensagens - 1]
                tipo_ultima_mensagem = ultima_mensagem.get_attribute('className')
                 
                tem_nova_mensagem = False
                enviar_saudacao = True

                if (num_mensagens == 1):
                    if ('message-in' in tipo_ultima_mensagem):
                        tem_nova_mensagem = True
                elif (num_mensagens > 1):
                     
                    if ('message-in' in tipo_ultima_mensagem):
                        tem_nova_mensagem = getTimePass(ultima_mensagem, 'client')

                        num_mensagens_bot = len(mensagens_bot)
                        if (num_mensagens_bot > 0):
                            ultima_mensagem_bot = mensagens_bot[num_mensagens_bot - 1]
                            enviar_saudacao = getTimePass(ultima_mensagem_bot, 'bot')
                                

                id = bot.driver.find_element_by_class_name("DP7CM").get_attribute('innerText')
            
                client = recupera_cliente_id(Clientes, id)
                  
                atualiza_listas_clientes(Clientes, ClientesEsperando, client)
     
                print(f'tem_nova_mensagem: {tem_nova_mensagem}')
                print(f'enviar_saudacao: {enviar_saudacao}')        
                if(tem_nova_mensagem == True):
                    time.sleep(3)

                    client = recupera_cliente_id(Clientes, id)
        
                    if (client == None):
                        client = Cliente(id)
                        Clientes.append(client)

                    print(f'client.estado :{client.estado}' )
                    if (client.estado == 0):
                        cliente_esperando_atendimento_humano = True
                    elif (client.estado == 1):
                        cliente_esperando_atendimento_humano = False

                    nome_cliente = " "
                    if (cliente_esperando_atendimento_humano  == False):
                        if (enviar_saudacao == True):
                            ultima_mensagem = bot.saudacao()
                            nome_cliente = bot.escuta(ultima_mensagem)
                        
                        print(f'nome_cliente: {nome_cliente}')
                        if (nome_cliente != None):
                           
                            mensagens = bot.driver.find_elements_by_class_name("_2hqOq")
                            num_mensagens = len(mensagens)
                            if (num_mensagens > 2):
                                try:
                                    penultima_mensagem = mensagens[num_mensagens - 2].find_element_by_class_name("_3Whw5").get_attribute('innerText')
                                    encontrou_penultima_mensagem = True
                                except:
                                    encontrou_penultima_mensagem = False
                            else:
                                encontrou_penultima_mensagem = False

                            print(f'encontrou_penultima_mensagem: {encontrou_penultima_mensagem}')
                            if (encontrou_penultima_mensagem == True):
                                
                                if (penultima_mensagem == bot.saudacao_manha or penultima_mensagem == bot.saudacao_tarde or penultima_mensagem == bot.saudacao_noite):
                                    bot.menu(nome_cliente) 
                                else:
                                    
                                   
                                    ultima_mensagem = mensagens[num_mensagens - 1].find_element_by_class_name("_3Whw5").get_attribute('innerText')

                                    print(f'ultima_mensagem:{ultima_mensagem}')

                                    opcao = ultima_mensagem

                                    if opcao == "0" or "zero" in opcao or "ZERO" in opcao or "Zero" in opcao:
                                        bot.menu()
                                    elif opcao == "01" or opcao == "1" or "um" in opcao or 'UM' in opcao or 'Um' in opcao or "Quem somos" in opcao or "quem somos" in opcao or "quem Somos" in opcao or "História" in opcao or "história" in opcao or "Historia" in opcao or "historia" in opcao:
                                        bot.quemSomos()
                                    elif opcao == "02" or opcao == "2" or "dois" in opcao or 'DOIS' in opcao or 'Dois' in opcao or "Localização" in opcao or "Localizacao" in opcao or "localização" in opcao or "localizacao" in opcao:
                                        bot.localizacao()
                                    elif opcao == "03" or opcao == "3" or "tres" in opcao or 'TRES' in opcao or 'Tres' in opcao or "Serviços" in opcao or "serviços" in opcao or "Servicos" in opcao or "servicos" in opcao or "servico" in opcao or "serviço" in opcao:
                                        bot.servicos()
                                    elif opcao == "04" or opcao == "4" or "quatro" in opcao or 'QUATRO' in opcao or 'Quatro' in opcao or "Contato" in opcao or "contato" in opcao or "contatos" in opcao or "Contatos" in opcao:
                                        bot.contato()
                                    elif opcao == "05" or opcao == "5" or "cinco" in opcao or 'CINCO' in opcao or 'Cinco' in opcao or "atendente" in opcao or "Atendente" in opcao or "Falar com atendente" in opcao or "falar com atendente" in opcao or "Falar com atendente (agendamento)" in opcao or "falar com atendente" in opcao or "Falar com atendente" in opcao or "falar com atendente" in opcao:
                                        bot.atendimento()   
                                        client.estado = 0
                                        ClientesEsperando.append(client)

                
                if (client != None):
                    if (client.estado == 0):
       
                        try:
                            ActionChains(bot.driver).context_click(contato).perform()
                            time.sleep(1)
                            contato.find_element_by_xpath("//*[text()='Marcar como não lida']").click()
                        except (WebDriverException, AttributeError, NoSuchAttributeException, ConnectionError, ElementNotVisibleException, ElementNotInteractableException, ElementNotSelectableException, ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException) as error:
                            print(str(error))


            time.sleep(1.5)
            i += 1

           


except (WebDriverException, ConnectionError, ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError, TimeoutException, AttributeError, NoSuchAttributeException) as Error:
    print(Error)
    bot.encerra()
