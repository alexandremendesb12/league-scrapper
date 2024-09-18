from collect_names import collect_names
from save_json import save_to_json

def main(number_of_pages):
    base_url = 'https://www.leagueofgraphs.com/pt/rankings/summoners/br/page-'

    all_names = []
    all_tags = []

    for page in range(1, number_of_pages + 1):  
        url = f"{base_url}{page}"
        names, tags = collect_names(url)
        all_names.extend(names)
        all_tags.extend(tags)

    save_to_json(all_names, 'names.json')  
    save_to_json(all_tags, 'tags.json')

if __name__ == '__main__':
    main(20)
