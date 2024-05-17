import requests
import json
import os
from bs4 import BeautifulSoup
import time

# Парсим основную инфу для обложки
def parseQuestsMainInfo(target_url, headers, seller_name):
    response = requests.get(target_url, headers=headers)

    if response.status_code == 200:
        pass
    else: print(response.status_code)

    answer = {
        "Квесты": []
    }

    soup = BeautifulSoup(response.text, 'html.parser')

    for article_tag in soup.find_all('article'):
        a_tags = article_tag.find_all('a')

        for a_tag in a_tags:                
            if a_tag.find('img'):
                item_obj = a_tag.find('img')
                item_image = item_obj['src']

            if "article__title" in a_tag.get('class', []):
                item_title = a_tag.get_text(strip=True)
            
            if "article__more" in a_tag.get('class', []):
                item_url = a_tag['href']


        answer['Квесты'].append({"Название": item_title, 
                                 "Картинка": item_image,
                                 "url": item_url
                                })

    with open(f"parsing_service/parsed_info/{seller_name}.json", 'w', encoding='utf-8') as data:
        json.dump(answer, data, ensure_ascii=False, indent=4)


def getJson(headers, directory):
    json_files = os.listdir(directory)
    main_url = "https://tarkov.help"

    for file in json_files:
        # Полный путь к файлу
        file_path = os.path.join(directory, file)

        # Получение имени файла с расширением
        file_name_with_extension = os.path.basename(file_path)

        # Получение имени файла без расширения
        file_name, file_extension = os.path.splitext(file_name_with_extension)

        # Проверяем, является ли файл JSON файлом
        if file_path.endswith('.json'):
            # Открываем и читаем JSON файл
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                # Проверяем наличие ключа "Квесты" в JSON данных
                if "Квесты" in data:
                    # Проходим по каждому квесту и извлекаем значение ключа "url"
                    for quest in data["Квесты"]:
                        quest_name = quest.get('Название')
                        if "url" in quest:
                            url = main_url + quest.get('url')
                            parseQuestsDetailedInfo(headers, url, file_name, quest_name)
                            

def parseQuestsDetailedInfo(headers, url:str, seller_name, quest_name):
    response = requests.get(url, headers=headers)

    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Извлекаем "Требования"
    requirements_text = ""
    requirements = soup.find('div', class_='quest-description__reqs')
    if requirements:
        requirements_text = "\n".join([span.get_text(separator="\n", strip=True) for span in requirements.find_all('span') if span.get_text(strip=True)])

    # Извлекаем "Цели квеста"
    goals_text = ""
    goals_section = soup.find('section', class_='quest-tab-goals-wrapper')
    if goals_section:
        goals = goals_section.find_all('div', class_='quest-tab-goal')
        goals_text = "\n".join(goal.find('p').get_text(separator="\n", strip=True) for goal in goals if goal.find('p'))

    # Ищем панель с наградамии за квест
    award_content = []

    award_section = soup.find('div', class_='quest-sub-column')
    if award_section:
        award_div = award_section.find('div', class_='quest-tab-grid _row')
        if award_div:
            award_text_div = award_div.find_all('div', class_='quest-text-award')

            for div in award_text_div:
                text = div.find('p').get_text()
                award_content.append(text)

    # Извлекаем "Как выполнить квест?" и исключаем div с тегами img, сохраняя ссылки на изображения
    guide_section = soup.find('section', class_='quest-guide')
    guide_content = []
    images = []

    for div in guide_section.find_all('div'):
        
        if "item-wrapper-inline" in div.get('class', []):
            text = div.find('a').get_text(separator=' ', strip=True)
            guide_content.append(text)
        
        # "bb-quest" not in 
        if not div.get('class', []):
            text = div.get_text(separator=' ', strip=True)
            guide_content.append(text)

        # "bb-quest" in 
        if not div.get('class', []):
            content_divs = div.find_all('div')

            for content_div in content_divs:
                if "bb-image__image" in content_div.get('class', []):
                    img_link_div = content_div.find('img')
                    img_link = img_link_div['src']
                    images.append(img_link)

    guide_text = " ".join(guide_content)
    award_text = "".join(award_content)

    getJsonDetailedData(requirements_text, goals_text, guide_text, images, award_text, quest_name, seller_name)

def getJsonDetailedData(requirements_text, goals_text, guide_text, images, award_text, quest_name, seller_name):
    data = {
        "Требования": requirements_text,
        "Цели квеста": goals_text,
        "Как выполнить квест": guide_text,
        "Ссылки на изображения": images,
        "Награды за квест": award_text
    }

    # if os.listdir(f'parsing_service/parsed_main_info/{seller_name}/{quest_name}'):
    #     pass
    # else:
    with open(f'parsing_service/parsed_detailed_info/{seller_name}/{quest_name}.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Словарь с продавцами и их ссылками 
    quests = {
        "Прапор" : "https://tarkov.help/ru/trader/prapor/quests",
        "Терапевт" : "https://tarkov.help/ru/trader/therapist/quests",
        "Скупщик" : "https://tarkov.help/ru/trader/fence/quests",
        "Лыжник" : "https://tarkov.help/ru/trader/skier/quests",
        "Миротворец" : "https://tarkov.help/ru/trader/peacemaker/quests",
        "Механик" : "https://tarkov.help/ru/trader/mechanic/quests",
        "Барахольщик" : "https://tarkov.help/ru/trader/ragman/quests",
        "Егерь" : "https://tarkov.help/ru/trader/jaeger/quests",
        "Смотритель" : "https://tarkov.help/ru/trader/lightkeeper/quests"
    }

    # Проверяем наличие файлов в каталоге
    if os.listdir("parsing_service/parsed_main_info"):
        pass
    
    else:
        for seller_name, target_url in quests.items():
            parseQuestsMainInfo(target_url, headers, seller_name)
    
    getJson(headers, 'parsing_service/parsed_main_info')

    