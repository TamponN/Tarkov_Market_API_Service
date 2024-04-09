from Config.apiConfig import target_url, secret_key
import requests

if __name__ == "__main__":
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': secret_key
    }

    query = 'Magazines'

    response = requests.get(target_url + "/items/all?tags=" + query, headers=headers)

    if response.status_code == 200:
        print(response.json())
    else: print(response.status_code)