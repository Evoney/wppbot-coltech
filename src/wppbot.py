# -*- coding: utf-8 -*-
import os
import time
import datetime


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class wppbot:
    dir_path = os.getcwd()

    saudacao_manha = "Bom dia, aqui quem fala é o chatbot da Coltech Consultoria. Para continuar seu atendimento, digite seu nome para que possamos salvar seu contato."
    saudacao_tarde = "Boa tarde, aqui quem fala é o chatbot da Coltech Consultoria. Para continuar seu atendimento, digite seu nome para que possamos salvar seu contato."
    saudacao_noite = "Boa noite, aqui quem fala é o chatbot da Coltech Consultoria. Para continuar seu atendimento, digite seu nome para que possamos salvar seu contato."

    def __init__(self):
        self.chrome = self.dir_path + '/chromedriver'

        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir=" + self.dir_path + "/profile/wpp")
        self.driver = webdriver.Chrome(self.chrome, chrome_options=self.options)

    def inicia(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.implicitly_wait(600)
        time.sleep(5)

    def saudacao(self):
        self.caixa_de_mensagem = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        hour = datetime.datetime.now().hour

        if (hour >= 6 and hour <= 12):
            mensagem = self.saudacao_manha
        elif (hour >= 12 and hour <= 18):
            mensagem = self.saudacao_tarde
        else:
            mensagem = self.saudacao_noite

        self.caixa_de_mensagem.send_keys(mensagem)
        time.sleep(1)
        self.botao_enviar = self.driver.find_element_by_class_name("_1U1xa")
        self.botao_enviar.click()
        return mensagem

        
    def escuta(self, penultimo_texto):
        time.sleep(1)
        cronometro = 1
        mensagens = self.driver.find_elements_by_class_name("_2hqOq")
        mensagem = len(mensagens) - 1
        ultimo_texto = mensagens[mensagem].find_element_by_css_selector('span.selectable-text').text
        print(f'ultimo_texto bot.escuta(): {ultimo_texto}')
        while (ultimo_texto == penultimo_texto):
            time.sleep(1)
            cronometro = cronometro + 1
            if (cronometro >= 15):
                break
            else:
                mensagens = self.driver.find_elements_by_class_name("_2hqOq")
                mensagem = len(mensagens) - 1
                penultimo_texto = ultimo_texto
                ultimo_texto = mensagens[mensagem].find_element_by_css_selector('span.selectable-text').text

        if (cronometro >= 15):
            return None
        else:
            return ultimo_texto

    # envia o menu para um contato
    def menu(self, nome_contato):
        img = self.dir_path + '/assets/menu.png'
        self.driver.find_element_by_css_selector('span[data-icon="clip"]').click()
        attach = self.driver.find_element_by_css_selector('input[type="file"]')
        attach.send_keys(img)
        time.sleep(2)

        self.caixa_de_mensagem = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]")
        self.caixa_de_mensagem.send_keys(f'{nome_contato}, durante nossa conversa, escolha e digite um número ou opção por vez para dar continuidade ao atendimento: ')
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys("1 - Quem somos")
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys("2 - Localização")
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys("3 - Serviços")
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys("4 - Contatos")
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys("5 - Falar com atendente")

        time.sleep(2)
        self.botao_enviar = self.driver.find_element_by_class_name("_3y5oW")
        self.botao_enviar.click()
        time.sleep(2)

    def localizacao(self):
        self.caixa_de_mensagem = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        localizacao = "https://goo.gl/maps/CMrWuunWRTrEk31p6"
        self.caixa_de_mensagem.send_keys(localizacao)
        time.sleep(6)
        self.botao_enviar = self.driver.find_element_by_class_name("_1U1xa")
        self.botao_enviar.click()

    def quemSomos(self):
        img = self.dir_path + '/assets/quemSomos.png'
        self.driver.find_element_by_css_selector('span[data-icon="clip"]').click()
        attach = self.driver.find_element_by_css_selector('input[type="file"]')
        attach.send_keys(img)
        time.sleep(2)
        
        self.caixa_de_mensagem = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]")
        self.caixa_de_mensagem.send_keys("A Coltech Consultoria é uma Empresa Júnior da Faculdade de Tecnologia da Universidade Federal do Amazonas. Fundada em 29 de abril de 2016, a Coltech é composta por alunos do curso de Engenharia Mecânica, Elétrica e Computação.")
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys("Já desenvolvemos mais de 50 projetos de alta qualidade e impacto no mercado, sendo nossos principais valores a transparência, o comprometimento, a postura empreendedora, o foco em resultados e o orgulho de ser Coltech!")
        time.sleep(2)
        self.botao_enviar = self.driver.find_element_by_class_name("_3y5oW")
        self.botao_enviar.click()
        time.sleep(2)


    def servicos(self):
        servicos = self.dir_path + '/assets/Carta de Serviços.pdf'
        self.driver.find_element_by_css_selector('span[data-icon="clip"]').click()
        attach = self.driver.find_element_by_css_selector('input[type="file"]')
        attach.send_keys(servicos)
        time.sleep(2)
        self.botao_enviar = self.driver.find_element_by_class_name("_3y5oW")
        self.botao_enviar.click()
        time.sleep(2)


    def atendimento(self):
        self.caixa_de_mensagem = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        desmarcar = "Atendimento de segunda a sexta-feira das 8h às 18h. Digite sua mensagem e " \
                    "aguarde alguns instantes para ser atendido."
        self.caixa_de_mensagem.send_keys(desmarcar)
        time.sleep(2)
        self.botao_enviar = self.driver.find_element_by_class_name("_1U1xa")
        self.botao_enviar.click()
        time.sleep(2)
      

    def contato(self):
        self.caixa_de_mensagem = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        self.caixa_de_mensagem.send_keys("Você pode entrar em contato por:")
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys("Presidência - (92) 991176606")
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys("Diretoria Comercial - (92) 99128-5495")
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        self.caixa_de_mensagem.send_keys("Atendimento: atendimento@coltechconsultoria.com.br")
        self.caixa_de_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
        time.sleep(2)
        self.botao_enviar = self.driver.find_element_by_class_name("_1U1xa")
        self.botao_enviar.click()
        time.sleep(2)
    

    def invalido(self):
        self.caixa_de_mensagem = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        invalido = "Entrada inválida. Por favor, digite outra opção do nosso Menu."
        self.caixa_de_mensagem.send_keys(invalido)
        time.sleep(2)
        self.botao_enviar = self.driver.find_element_by_class_name("_1U1xa")
        self.botao_enviar.click()

    def encerra(self):
        self.driver.quit()
