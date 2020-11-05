import json
from pprint import pprint
from hash import get_hash

data_list = []

class Parser:
    def __init__(self, list_of_countries):
        self.list_of_countries = list_of_countries
        self.current_country_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_country_index == len(self.list_of_countries):
            with open("country_info.json", "a", encoding='utf8') as file:
                json.dump(data_list, file, ensure_ascii=False, indent=0)
            raise StopIteration
        country_name = self.list_of_countries[self.current_country_index]
        self.current_country_index += 1
        data_list.append({country_name: f'https://en.wikipedia.org/wiki/{country_name.replace(" ", "_")}'})
        return


with open("countries.json", "r") as f:
    data_countries = json.load(f)

country_list = [country['name']['common'] for country in data_countries]


if __name__ == '__main__':
    for data_url in Parser(country_list):
        pprint(data_url)

    for i in get_hash('country_info.json'):
        print(i)
