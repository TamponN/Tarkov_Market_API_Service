from bs4 import BeautifulSoup
import requests
import json

def parseQuests():
    pass

def getJson():
    pass

if __name__ == "__main__":
    target_url = "https://tarkov.help/ru/search/entities/suggestion"

    target_search_item = 'Ору'

    payload = {
        "searchEntities": ["Quest", "Item"],
        "query": target_search_item
    }

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.post(target_url, json=payload, headers=headers)

    if response.status_code == 200:
        # print(response.text)
        pass
    else: print(response.status_code)

    answer = {
        "Предметы": [],
        "Квесты": []
    }

    soup = BeautifulSoup(response.text, 'html.parser')

    for li_tag in soup.find_all('li', attrs={'data-bsgid': True}):
        a_tag = li_tag.find('a')
        if a_tag:
            item_title = a_tag.get_text(strip=True)
            item_url = a_tag['href']
            answer["Предметы"].append({"Название": item_title, "URL": item_url},)

    for li_tag in soup.find_all('li', attrs={'title': True, 'data-bsgid': False}):
        a_tag = li_tag.find('a')
        if a_tag:
            item_title = a_tag.get_text(strip=True)
            item_url = a_tag['href']
            answer["Квесты"].append({"Название": item_title, "URL": item_url}, )

    with open("answer.json", 'w', encoding='utf-8') as data:
        json.dump(answer, data, ensure_ascii=False, indent=4)
