import requests
from bs4 import BeautifulSoup

def get_english_words():
    url = "https://plitkanadom.ru/"
    response = requests.get(url)
    #print(response.text)
    soup = BeautifulSoup(response.content, "html.parser")
    english_words = soup.find_all("img", alt="Техническая пробка")


    print(english_words)


get_english_words()
