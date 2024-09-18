import requests
from bs4 import BeautifulSoup

def collect_names(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        names = soup.find_all('span', class_='name')
        
        name_list = []
        tag_list = []
        for name in names:
            full_name = name.get_text()
            if '#' in full_name:
                name_part, tag_part = full_name.split('#', 1)
                name_list.append(name_part.strip())
                tag_list.append(tag_part.strip())
            else:
                name_list.append(full_name.strip())
                tag_list.append('')  # Caso não tenha tag, adiciona uma tag vazia
        
        return name_list, tag_list
    else:
        print(f"Erro ao acessar a página {url}. Status code: {response.status_code}")
        return [], []