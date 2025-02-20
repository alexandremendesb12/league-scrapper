# League Scraper

O League Scraper é uma ferramenta desenvolvida em Python para coletar nomes de jogadores, tags e informações regionais a partir do site League of Graphs. Os dados coletados são salvos em um arquivo JSON, facilitando sua reutilização em outros projetos.

## Funcionamento

### Instalação

O projeto é instalado localmente, utilizando o gerenciador de pacotes pip. É necessário criar um ambiente virtual e instalar as dependências listadas no arquivo `requirements.txt`.

### Configuração

O projeto utiliza um arquivo de configuração `constants.py` para armazenar as constantes utilizadas no projeto, como a URL base do site League of Graphs e o nome do arquivo de saída.

### Coleta de dados

O projeto utiliza a biblioteca `requests` para fazer requisições HTTP ao site League of Graphs e coletar os dados dos jogadores. A coleta de dados é realizada em paralelo, utilizando a biblioteca `concurrent.futures`.

### Processamento de dados

Os dados coletados são processados utilizando a biblioteca `pandas` e transformados em um DataFrame.

### Salvamento de dados

Os dados processados são salvos em um arquivo JSON, utilizando a biblioteca `json`.

## Uso

### Execução

O projeto é executado utilizando o comando `python main.py`.

### Entrada de dados

O usuário é solicitado a entrar com a região e o número de páginas que deseja coletar.

### Saída

O projeto salva os dados coletados em um arquivo JSON, chamado `players_data.json`.

## Estrutura do projeto

* `src`: Pasta que contém o código fonte do projeto.
	+ `main.py`: Arquivo principal do projeto, responsável por executar a coleta e processamento de dados.
	+ `scraper.py`: Arquivo responsável por coletar os dados do site League of Graphs.
	+ `processor.py`: Arquivo responsável por processar os dados coletados.
	+ `utils`: Pasta que contém arquivos de utilidades, como a classe `FileLoader` e a classe `FileSaver`.
	+ `constants.py`: Arquivo de configuração que armazena as constantes utilizadas no projeto.

## Requisitos

* Python 3.7 ou superior
* Bibliotecas listadas no arquivo `requirements.txt`

## Licença

O projeto é licenciado sob a Licença Apache 2.0. Consulte o arquivo `LICENSE` para mais detalhes.
