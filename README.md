# Coletor de Nomes e Tags de Jogadores

Este projeto coleta **nomes** e **tags** de jogadores da página [League of Graphs](https://www.leagueofgraphs.com/pt/rankings/summoners) e os salva em dois arquivos JSON: um contendo os **nomes** e outro contendo as **tags**.

## Como executar

1. **Clone ou baixe este repositório para sua máquina local**.

2. **Instale as dependências necessárias**:

   No terminal, navegue até o diretório do projeto e execute o seguinte comando para instalar as bibliotecas necessárias (como `requests` e `BeautifulSoup`):

   ```bash
   pip install -r requirements.txt

3. **Execute o arquivo main.py no terminal**:

   No terminal, execute o seguinte comando para iniciar o processo de coleta de dados:

    ```bash  
    python main.py

  Isso iniciará o processo de scraping e salvará os resultados nos arquivos names.json (contendo apenas os nomes) e tags.json (contendo apenas as tags), 
  localizados no diretório do projeto.

**Alterando o número de registros**

Por padrão, o código coleta os registros de 100 jogadores por página. Se você quiser obter mais registros, basta alterar o número de páginas processadas no arquivo main.py.

**Modificando o número de páginas**

Dentro da função main(), cada página corresponde a um GET que coleta os dados de 100 jogadores. Para aumentar o número de páginas, você pode alterar o valor passado na chamada da função main().

Exemplo:

Se você quiser processar 5 páginas (500 jogadores), abra o arquivo main.py e altere a linha dentro do bloco if __name__ == '__main__': para:
  ```bash
    if __name__ == '__main__':
    main(5)  # Altere o valor '5' para o número de páginas que deseja processar


