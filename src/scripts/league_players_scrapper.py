import requests
from bs4 import BeautifulSoup
from typing import Dict, List

class LeaguePlayersScrapper:
    def __init__(self, url: str = None):
        self.url = url

    def collect_names(self, url: str = None, region: str = None) -> List[Dict[str, str]]:
        """
        Coleta nomes, tags e região de jogadores a partir de uma página fornecida.

        Args:
            url (str): URL da página para coleta. Usa self.url se não for fornecida.
            region (str): Região associada aos jogadores.

        Returns:
            list: Lista de dicionários contendo nome, tag e região.
        """
        target_url = url or self.url
        if not target_url:
            raise ValueError("Nenhuma URL foi fornecida para coleta.")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        response = requests.get(target_url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            names = soup.find_all('span', class_='name')
            
            players_data = []
            for name in names:
                full_name = name.get_text()
                if '#' in full_name:
                    name_part, tag_part = full_name.split('#', 1)
                    players_data.append({
                        'name': name_part.strip(),
                        'tag': tag_part.strip(),
                        'region': region or ''
                    })
                else:
                    players_data.append({
                        'name': full_name.strip(),
                        'tag': '',
                        'region': region or ''
                    })
            
            return players_data
        else:
            print(f"Erro ao acessar a página {target_url}. Status code: {response.status_code}")
            return []
        