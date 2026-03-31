from re import findall
from requests import get
from os import mkdir

class Parser():
    def __init__(self, pLink, pName):
        self.link = pLink
        if not pName:
            pName = self.link.replace("https://telegra.ph/", "")
        self.name = pName
        self.data = ""
        self.links = []
        self.images = []

    def download(self):
        mkdir(self.name)
        self.page()
        self.parse()
        for i in range(len(self.links)):
            print(f"Скачивание изображения №{i + 1}")
            self.image(i)

    def page(self):
        response = get(self.link)
        if response.status_code == 200:
            self.data = response.text
            print("HTML страница успешно скачана")
        else:
            print(f"Ошибка при загрузке страницы: {response.status_code}")

    def parse(self):
        self.links = findall(r'<img src="([^"]+)"', self.data)
        if self.links:
            print(f"Найдено {len(self.links) + 1} изображений")
        else:
            print("Мы не нашли ни одного изображения :(")

    def image(self, i):
        link = self.links[i]
        try:
            response = get(link)
            if response.status_code == 200:
                with open(f"{self.name}/{i}.jpg", "wb") as file:
                    file.write(response.content)
                print(f"Картинка успешно скачана и сохранена как '{i}.jpg'")
            else:
                print(f"Ошибка при загрузке картинки: {response.status_code}")
        except:
            print("Неизвестная ошибка")

link = input("Пожалуйста, введите ссылку на ресурс: ")
name = input("Пожалуйста, введите имя для папки сохранения (Enter для автоматического названия): ")
parser = Parser(link, name)
parser.download()