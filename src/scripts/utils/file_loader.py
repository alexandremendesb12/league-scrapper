import json 

class FileLoader:
    @staticmethod
    def load_json(file_name: str) -> dict:
        """Loads a JSON file and returns its data as a dictionary.

        Args:
            file_name (str): The path to the JSON file.

        Returns:
            dict: A dictionary containing the data from the JSON file.
        """
        with open(file_name) as file:
            data = json.load(file)

        return data
