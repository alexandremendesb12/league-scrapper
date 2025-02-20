import pandas as pd
import os
from .utils.file_loader import FileLoader

class Processor:
    """Processa dados de jogadores em um Dataframe do Pandas."""
    def __init__(self):
        self.loader = FileLoader()
        """Inicia a classe Processor.
        
        Essa classe tem como objetivo processar os dados de jogadores em um Dataframe do Pandas.
        """

    def transform_to_pandas(self, json_file_path: str) -> pd.DataFrame:
        """Transforma dados de jogadores em um Dataframe do Pandas.
        
        Args:
            json_file_path (str): Caminho do arquivo JSON com os dados dos jogadores.
        
        Returns:
            pd.DataFrame: Dataframe com os dados dos jogadores.
        """
        data = self.loader.load_json(json_file_path)
        df = pd.DataFrame(data)
        return df

if __name__ == '__main__':
    file_path = os.path.join('src','temp','players_data.json')
    df = Processor().transform_to_pandas(file_path)
    print(df)
    
    