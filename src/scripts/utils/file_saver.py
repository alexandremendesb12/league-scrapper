from typing import List, Dict
import json
import os

class FileSaver:
    @staticmethod
    def _save_to_json(data: List[Dict[str, str]], filename: str):
        """
        Salva dados em um arquivo JSON.

        Args:
            data (list): Lista de dicionários com os dados a serem salvos.
            filename (str): Nome do arquivo.
        """
        temp_dir = os.path.join('src', 'temp')
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        with open(os.path.join(temp_dir,filename), 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    def save_data_json(self, data: List[Dict[str, str]], filename: str) -> None:
        """
        Salva dados em um arquivo JSON.

        Args:
            data (list): Os dados a serem salvos.
            filename (str): O nome do arquivo.
        """
        try:
            self._save_to_json(data, filename)
            print(f"Dados salvos com sucesso em '{filename}'.")
        except Exception as e:
            print(f"Erro ao salvar dados em '{filename}': {e}")
