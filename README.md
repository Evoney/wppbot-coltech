
<h1 align="center">
Whatsapp Bot Coltech
</h1>
<p align="center">
<img alt="last commit" src="https://img.shields.io/github/last-commit/evoney/wpp-coltech?color=blue">
<img alt="progress" src="https://img.shields.io/badge/status-in_progress-blue">
</p>
<h4 align="center">
	<a href="#pencil-sobre-o-projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#rocket-stack">Stack</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#blue_book-configurando-ambiente">Configurando ambiente</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#dart-rodando-aplicação">Rodando aplicação</a>
</h4>

 
 ## :pencil: Sobre o projeto 
**Resumo**: Este projeto tem por objetivo automatizar serviços de atendimento via whatsapp 

**Objetivo**: 
Integrar tecnologias de automação ao whatsapp 

## :rocket: Stack
<p align="center">
<img alt="Selenium" src="https://img.shields.io/badge/Selenium-Python-blue?style=for-the-badge&logo=dependabot">
</p>

## :blue_book: Configurando ambiente

  
Antes de começar, é preciso ter duas ferramentas instaladas:
- **Pyenv** :  Permite que você instale outras versões do python em sua máquina
- **Virtualenv**: Permite criar ambientes virtuais em sua máquina
 
 Instalação para linux:
 ```bash
 # clone o projeto
 git https://github.com/Evoney/wppbot-coltech.git
 # instale a versão mais recente do python  
 pyenv install 3.8.3

 # Com virtualenv:
 # crie uma máquina virtual a partir dela
 virtualenv -p ~/.pyenv/versions/3.8.3/bin/python nome_da_máquina_virtual
 # ative sua máquina virtual
 source nome_da_máquina_virtual/bin/activate
 
 #Com pyenv:
 # crie uma máquina virtual a partir dela
 pyenv virtualenv 3.8.3 nome_da_máquina_virtual 
  # ative sua máquina virtual
 pyenv activate nome_da_máquina_virtual

 # Por fim, instale as tecnologias utilizadas
 pip install -r requirements.txt
```

Instalação para windows:
```bash
# Crie uma máquina virtual com a versão mais recente do python:
"python -m virtualenv nome_da_máquina_virtual" 
# Ative sua máquina virtual
"nome_da_máquina_virtual\Scripts\activate"
```
  

## :dart: Rodando aplicação

Para iniciar a aplicação, é necessário baixar o chromedriver com a mesma versão do seu navegador
Para verificar a sua versão do google chrome vá em:
Opções > Ajuda > Sobre o Google Chrome 
[**Chromedriver**](https://chromedriver.chromium.org/downloads)

Mova o arquivo para a pasta **src** 
Sua estrutura deverá estar assim: 
```bash
/src
    /assets
    /classes
    chromedriver
    main.py
    wppbot.py
setup.py
requeriments.txt
...
```
Para testes em ambiente linux, você deverá executar:

```bash
python main.py
```

Para criação do executável em windows: 
```bash
python setup.py install 
```

## Bom code! ##