## Descrição do Projeto
<p>Projeto desenvolvido para a disciplina de Sistemas Distribuídos. O projeto se baseia num sistema distribuído de arquitetura cliente-servidor, de modo que este objetiva possibilitar aos seus usários a criação de nuvens de palavras de maneira ágil e rápida a partir de um texto.</p>

Tabela de conteúdos
=================
<!--ts-->
   * [Como usar](#como-usar)
      * [Pre Requisitos](#pre-requisitos)
      * [Arquivos](#arquivos)
   * [Tecnologias](#tecnologias)
   * [Funcionalidades implementadas](#funcionalidades-implementadas)
   * [Funcionalidades futuras](#funcionalidades-futuras)
   
<!--te-->

## Como usar

### Pre Requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python3](https://www.python.org/downloads/). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

Antes de tudo, clone este repositório e instale as dependências com:
```bash
#Clone o repositório
$ git clone <https://github.com/luizsfjr/Projeto-FreeWordCloud>
# Instale as dependências
$ pip install -r requirements.txt
```


#### Rodando o Servidor

```bash
# Acesse a pasta do projeto no terminal/cmd
$ cd Projeto-FreeWordCloud
# Acesse a pasta do Servidor no terminal/cmd
$ cd Servidor
# Execute o servidor
$ python3 -u main.py
# A parte do servidor inciará na porta:5000
```

#### Rodando o Cliente

```bash
# Acesse a pasta do projeto no terminal/cmd
$ cd Projeto-FreeWordCloud
# Acesse a pasta do Cliente no terminal/cmd
$ cd Cliente
# Execute o cliente
$ python3 -u main.py
# A parte do cliente inciará na porta:8000 - acesse <http://127.0.0.1:8000> 
```
### Arquivos
  #### Cliente
        * Static
          * css
            * style.css
          * images
            * wordcloud.png
        * Templates
          * index.html
        * main.py
  #### Servidor
        * main.py
        * Preprocessing.py
        * Wordcloud.py
        * utils.py
  #### requirements.txt
  
## Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [NLTK](https://www.nltk.org/)
- [WordCloud](https://pypi.org/project/wordcloud/)
- [CairoSVG](https://cairosvg.org/)

## Funcionalidades implementadas
  - Módulos de pré-processamento
  - Geração da nuvem de palavras
  - Aplicações cliente e servidor 100% prontas
  - Opções de estilização da nuvem de palavras, como background e tema.
  - Download da nuvem de palavras
## Comunicação entre os sistemas
  - Presente no arquivo main da parte do cliente, indicado pelos comentários nas linhas 20 e 21
## Última entrega
  - Inclusão de tratamento de erro
  - Simplificação de código para maior legibilidade
  - Inclusão de estilização da nuvem por tema
