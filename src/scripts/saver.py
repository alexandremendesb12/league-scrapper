from typing import List, Dict
import json

class FileSaver:
    @staticmethod
    def save_to_json(data: List[Dict[str, str]], filename: str):
        """
        Salva dados em um arquivo JSON.

        Args:
            data (list): Lista de dicionários com os dados a serem salvos.
            filename (str): Nome do arquivo.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
