
# League Scrapper

O **League Scrapper** é uma ferramenta desenvolvida em Python para coletar nomes de jogadores, tags e informações regionais a partir do site [League of Graphs](https://www.leagueofgraphs.com). Os dados coletados são salvos em um arquivo JSON, facilitando sua reutilização em outros projetos.

## Recursos

- Coleta dados de jogadores de várias páginas simultaneamente.
- Suporta múltiplas regiões.
- Salva os dados em formato JSON para fácil integração com outros sistemas.

## Instalação

Como o projeto não está mais disponível no PyPI, a instalação deve ser feita localmente. Siga os passos abaixo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/alexandremendesb12/league-scrapper.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd league-scrapper
   ```

3. Crie um ambiente virtual (recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

Após a instalação, você pode utilizar o League Scrapper em seus scripts Python.

### Exemplo de Uso

```python
from league_scrapper import LeagueScrapper

# Inicializa o scrapper para uma região específica
scrapper = LeagueScrapper(region='br')

# Coleta dados de jogadores
dados_jogadores = scrapper.coletar_dados(paginas=5)

# Salva os dados em um arquivo JSON
scrapper.salvar_dados(dados_jogadores, 'dados_jogadores.json')
```

Este exemplo inicializa o scrapper para a região brasileira, coleta dados de 5 páginas de jogadores e salva as informações no arquivo `dados_jogadores.json`.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a Licença Apache 2.0. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

*Nota: Este projeto não é afiliado ao League of Legends ou ao League of Graphs.*
