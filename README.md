
# **League Scrapper**

O **League Scrapper** é uma biblioteca Python para coletar **nomes**, **tags**, e informações regionais de jogadores a partir da página [League of Graphs](https://www.leagueofgraphs.com/pt/rankings/summoners). Os dados coletados são salvos em um arquivo JSON para fácil reutilização em outros projetos.

## **Recursos**
- Coleta dados de jogadores de várias páginas simultaneamente.
- Suporte para múltiplas regiões.
- Dados salvos em formato JSON para integração em outros sistemas.

---

## **Instalação**
### **Via PyPI**
Instale diretamente do [PyPI](https://pypi.org/project/league-scrapper/):
```bash
pip install league-scrapper
```

### **Manual**
1. Clone o repositório:
   ```bash
   git clone https://github.com/alexandremendesb12/league-scrapper.git
   cd league-scrapper
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Instale o pacote localmente:
   ```bash
   pip install .
   ```

---

## **Como Usar**

### **Exemplo de Uso**
Aqui está um exemplo básico de como usar a biblioteca para coletar e salvar dados:
```python
from league_scrapper import Main

# Configuração do coletor
scrapper = Main()

# Coleta dados de 5 páginas da região "br"
data = scrapper.collect_data(number_of_pages=5, region="br")

# Salva os dados em um arquivo JSON
scrapper.save_data(data, "dados_jogadores.json")
```

### **Parâmetros**
- `number_of_pages` (int): Número de páginas a serem coletadas. Cada página contém até 100 jogadores.
- `region` (str): Região para buscar os jogadores (ex.: "br", "euw", "na").

---

## **Estrutura do Projeto**

- **league_scrapper/**
  - `__init__.py`: Arquivo de inicialização do pacote.
  - `main.py`: Arquivo principal para execução.
  - **scripts/**
    - `league_players_scrapper.py`: Responsável por realizar o scraping dos dados.
    - `saver.py`: Utilitário para salvar os dados em formato JSON.

---

## **Funcionalidades Avançadas**

### **Requisições Simultâneas**
Se o número de páginas a ser processado for maior que 5, o código utiliza `ThreadPoolExecutor` para melhorar o desempenho.

### **Execução via Terminal**
O projeto pode ser executado diretamente no terminal:
```bash
python -m league_scrapper.main
```

Você será solicitado a inserir:
1. A região dos jogadores (ex.: "br").
2. O número de páginas que deseja processar.

---

## **Contribuições**
Sinta-se à vontade para abrir **issues** ou enviar **pull requests** para melhorias no projeto. 

---

## **Licença**
Este projeto está licenciado sob a [MIT License](LICENSE).
