from .scripts.scraper import Scraper
from .scripts.utils.file_saver import FileSaver
from .scripts.utils.constants import DATA_FILE, BASE_URL

class Main():
    def __init__(self):
        self.collector = Scraper(BASE_URL)
        self.saver = FileSaver()

    def run(self) -> None:
        try:
            print("Caso não queira utilizar algum dos campos a seguir em sua busca, apenas pressione ENTER")

            region = str(input("Região: ")).strip()
            number_of_pages = int(input("Quantidade de páginas: "))

            if number_of_pages < 1:
                raise ValueError("O número de páginas deve ser maior que 0.")

            print("Iniciando a coleta de dados...")
            all_players_data = self.collector.collect_data(number_of_pages=number_of_pages, region=region)

            print("Salvando dados em json...")
            self.saver.save_data_json(all_players_data, DATA_FILE)

            print("Processo concluído com sucesso!")
        except ValueError as e:
            print(f"Entrada inválida: {e}")
        except KeyboardInterrupt:
            print("\nProcesso interrompido pelo usuário.")
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == '__main__':
    Main().run()
