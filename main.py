import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/107.0.0.0 Safari/537.36'
}
#Если прокси привязан к IP простой словарь, если через логин и пароль словарь имеет вид:
# proxies = {
#     'https': 'http:{login}:{password}@//45.136.246.25:8000'
# }
proxies = {
    'https': 'http://45.136.246.25:8000'
}


def get_location(url):
    response = requests.get(url=url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.text, 'lxml')
    ip = soup.find('div', class_='ip').text.strip()
    location = soup.find('div', class_='value-country').text.strip()
    print(f"IP: {ip}\nLOCATION: {location}")# строчка для проверки


def main():
    get_location(url='https://2ip.ru')


if __name__ == "__main__":
    main()
