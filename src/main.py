from .scripts.league_players_scrapper import LeaguePlayersScrapper
from .scripts.saver import FileSaver
from typing import Dict, List
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = 'https://www.leagueofgraphs.com/pt/rankings/summoners'
DATA_FILE = 'players_data.json'

class LeagueScrapper():
    def __init__(self):
        self.collector = LeaguePlayersScrapper(BASE_URL)
        self.saver = FileSaver()

    def collect_data(self, number_of_pages: int, region: str) -> List[Dict[str, str]]:
        """
        Coleta dados de jogadores de um número específico de páginas.

        Args:
            number_of_pages (int): O número de páginas a serem coletadas.
            region (str): Região dos jogadores.

        Returns:
            list: Lista de dicionários contendo nome, tag e região.
        """
        all_players_data = []
        urls = [f"{BASE_URL}/{region}/page-{page}" for page in range(1, number_of_pages + 1)]

        if number_of_pages > 5:
            print("Usando requisições concorrentes com ThreadPoolExecutor...")
            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = {executor.submit(self.collector.collect_names, url): url for url in urls}

                for future in as_completed(futures):
                    url = futures[future]
                    try:
                        players_data = future.result()
                        for player in players_data:
                            player["region"] = region
                        all_players_data.extend(players_data)
                    except Exception as e:
                        print(f"Erro ao processar a URL {url}: {e}")
        else:
            print("Usando requisições sequenciais...")
            for url in urls:
                print(f"Coletando dados da página: {url}")
                try:
                    players_data = self.collector.collect_names(url)
                    for player in players_data:
                        player["region"] = region
                    all_players_data.extend(players_data)
                except Exception as e:
                    print(f"Erro ao coletar dados da página {url}: {e}")

        return all_players_data

    def save_data(self, data: List[Dict[str, str]], filename: str) -> None:
        """
        Salva dados em um arquivo JSON.

        Args:
            data (list): Os dados a serem salvos.
            filename (str): O nome do arquivo.
        """
        try:
            self.saver.save_to_json(data, filename)
            print(f"Dados salvos com sucesso em '{filename}'.")
        except Exception as e:
            print(f"Erro ao salvar dados em '{filename}': {e}")

    def run(self) -> None:
        """
        Ponto de entrada do programa.
        """
        try:
            print("Caso não queira utilizar algum dos campos a seguir em sua busca, apenas pressione ENTER")

            region = str(input("Região: ")).strip()
            number_of_pages = int(input("Quantidade de páginas: "))

            if number_of_pages < 1:
                raise ValueError("O número de páginas deve ser maior que 0.")

            print("Iniciando a coleta de dados...")
            all_players_data = self.collect_data(number_of_pages=number_of_pages, region=region)

            print("Salvando dados...")
            self.save_data(all_players_data, DATA_FILE)

            print("Processo concluído com sucesso!")
        except ValueError as e:
            print(f"Entrada inválida: {e}")
        except KeyboardInterrupt:
            print("\nProcesso interrompido pelo usuário.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == '__main__':
    LeagueScrapper().run()
