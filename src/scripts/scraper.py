import requests
from bs4 import BeautifulSoup
from typing import Dict, List
from typing import Dict, List
from concurrent.futures import ThreadPoolExecutor, as_completed

class Scraper:
    def __init__(self, url: str = None):
        self.url = url

    def collect_names(
        self, url: str, region: str
    ) -> List[Dict[str, str]]:
        """
        Collects player names, tags, and regions from a specified webpage.

        Args:
            url (str): The URL of the page to collect data from.
            region (str): The region associated with the players.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing
                name (str): The player's name.
                tag (str): The player's tag.
                region (str): The region associated with the player.
        """
        if not url:
            raise ValueError("A URL must be provided for data collection.")

        headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            )
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to access the page {url}. Status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser', parse_only=BeautifulSoup.SoupStrainer('span', class_='name'))

        return [
            {
                'name': name.get_text().split('#', 1)[0].strip(),
                'tag': name.get_text().split('#', 1)[1].strip() if '#' in name.get_text() else '',
                'region': region
            }
            for name in soup
        ]
    
    def collect_data(self, number_of_pages: int, region: str) -> List[Dict[str, str]]:
        """
        Collects data from a specified number of pages.

        Args:
            number_of_pages (int): The number of pages to collect from.
            region (str): The region of the players.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing
                name (str): The player's name.
                tag (str): The player's tag.
                region (str): The region associated with the player.
        """
        urls = [
            f"{self.url}/{region}/page-{page}"
            for page in range(1, number_of_pages + 1)
        ]

        all_players_data = []
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(self.collect_names, url, region): url for url in urls}

            for future in as_completed(futures):
                try:
                    players_data = future.result()
                    all_players_data.extend(players_data)
                except Exception as e:
                    print(f"Error processing URL {urls[futures[future]]}: {e}")

        return all_players_data
