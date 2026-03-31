# 📥 Telegram Parser / Парсер Telegram-публикаций

<div align="center">

![Version](https://img.shields.io/badge/версия-1.0.0-brightgreen.svg?style=for-the-badge&labelColor=black)
![License](https://img.shields.io/badge/лицензия-MIT-blue.svg?style=for-the-badge&labelColor=black)
![Python](https://img.shields.io/badge/Python-3.x-3776AB.svg?style=for-the-badge&labelColor=black&logo=python)
![Requests](https://img.shields.io/badge/зависимости-1-important.svg?style=for-the-badge&labelColor=black)
![Human written](https://img.shields.io/badge/написано-человеком-ff69b4.svg?style=for-the-badge&labelColor=black)

**✨ Простой инструмент для скачивания изображений из публикаций Telegram ✨**

</div>

---

## 📋 Содержание

<details>
<summary><b>🇷🇺 Русская версия</b></summary>

<br>

- [🚀 Запуск проекта](#-запуск-проекта)
- [📝 Описание проекта](#-описание-проекта)
- [✨ Ключевые возможности](#-ключевые-возможности)
- [🎯 Зачем здесь класс?](#-зачем-здесь-класс)
- [⚙️ Как это работает](#️-как-это-работает)
- [📁 Структура проекта](#-структура-проекта)
- [📊 Достоинства и недостатки](#-достоинства-и-недостатки)
- [🔮 Планы по развитию](#-планы-по-развитию)
- [🐛 Известные проблемы](#-известные-проблемы)
- [📜 Лицензия](#-лицензия)
- [👨‍💻 Для разработчиков](#-для-разработчиков)

</details>

<details>
<summary><b>🇬🇧 English version</b></summary>

<br>

- [🚀 Project Launch](#-project-launch)
- [📝 Project Description](#-project-description)
- [✨ Key Features](#-key-features)
- [🎯 Why a Class?](#-why-a-class)
- [⚙️ How It Works](#️-how-it-works)
- [📁 Project Structure](#-project-structure)
- [📊 Advantages and Disadvantages](#-advantages-and-disadvantages)
- [🔮 Development Plans](#-development-plans)
- [🐛 Known Issues](#-known-issues)
- [📜 License](#-license)
- [👨‍💻 For Developers](#-for-developers)

</details>

---

## 🇷🇺 Русская версия

### 🚀 Запуск проекта

#### Локальный запуск
```bash
# Клонируйте репозиторий
git clone https://github.com/ваш-username/telegram-parser.git

# Перейдите в папку проекта
cd telegram-parser

# Установите единственную зависимость
pip install requests

# Запустите парсер
python parser.py
```

#### Требования
- Python 3.x
- Библиотека: `requests` (единственная зависимость)
- Интернет-соединение

---

### 📝 Описание проекта

**Telegram Parser** — это простой инструмент для скачивания всех изображений из публикаций на платформе Telegra.ph (и других сайтах с аналогичной структурой). Проект создан в учебных целях для практики работы с:

- **Классами в Python** — инкапсуляция логики парсинга
- **Регулярными выражениями** — поиск ссылок на изображения
- **HTTP-запросами** — загрузка HTML-страниц и изображений
- **Работой с файловой системой** — создание папок и сохранение файлов

---

### ✨ Ключевые возможности

| Категория | Функция | Описание |
|-----------|---------|----------|
| 🌐 **Парсинг** | Загрузка HTML | Получение исходного кода страницы |
| | Поиск изображений | Автоматическое извлечение всех ссылок на картинки |
| | Регулярные выражения | Поиск по шаблону `<img src="...">` |
| 💾 **Сохранение** | Автоматическое именование | Создание папки с заданным или автоматическим именем |
| | Пакетная загрузка | Скачивание всех найденных изображений |
| | Нумерация файлов | Сохранение как `0.jpg`, `1.jpg`, `2.jpg`... |
| 🛡️ **Надёжность** | Обработка ошибок | Проверка статусов HTTP-ответов |
| | Информирование | Подробный вывод процесса работы |

---

### 🎯 Зачем здесь класс?

**Я изучаю Python, поэтому пытаюсь практиковаться в ООП!** 🐍

Использование класса `Parser` в этом проекте — сознательное решение для отработки навыков объектно-ориентированного программирования:

| Преимущество | Как это реализовано |
|--------------|---------------------|
| **Инкапсуляция** | Все данные (ссылка, имя папки, HTML, списки) хранятся внутри объекта |
| **Модульность** | Каждый метод отвечает за одну задачу: `page()`, `parse()`, `image()` |
| **Переиспользование** | Можно создать несколько парсеров для разных ссылок без конфликтов |
| **Расширяемость** | Легко добавить новые форматы (PDF, видео) через наследование |
| **Читаемость** | Код организован логически, легко понять поток работы |

**Без класса** этот же код можно было бы написать как набор функций и глобальных переменных, но класс позволяет:
- Хранить состояние между вызовами методов
- Легко передавать объект в другие функции
- Понять концепцию `self` и работы с атрибутами экземпляра

Это **учебный проект**, поэтому здесь есть то, что я хочу изучить и закрепить на практике.

---

### ⚙️ Как это работает

```
1. Пользователь вводит ссылку на публикацию
                ↓
2. Создаётся объект Parser(link, folder_name)
                ↓
3. Вызывается метод download()
                ↓
4. Создаётся папка для сохранения
                ↓
5. page() — загружает HTML страницы
                ↓
6. parse() — ищет все ссылки на изображения
                ↓
7. image(i) — скачивает каждое изображение по очереди
                ↓
8. Готово! Все картинки сохранены в папку
```

#### Пример работы

```python
parser = Parser("https://telegra.ph/Пример-публикации-01-01", "my_images")
parser.download()

# Вывод:
# HTML страница успешно скачана
# Найдено 5 изображений
# Скачивание изображения №1
# Картинка успешно скачана и сохранена как '0.jpg'
# ...
```

---

### 📁 Структура проекта

```
📦 telegram-parser
├── 📄 parser.py          # Основной файл парсера
├── 📄 README.md          # Документация
├── 📄 DEVELOPER.md       # Техническая документация
└── 📁 my_images/         # Папка с загруженными изображениями (создаётся при запуске)
    ├── 0.jpg
    ├── 1.jpg
    └── ...
```

---

### 📊 Достоинства и недостатки

#### ✅ Достоинства
- **✍️ Учебный характер** — код написан для практики, понятен начинающим
- **📦 Минимум зависимостей** — всего **1** библиотека (`requests`)
- **🧩 Модульная структура** — класс разбит на логические методы
- **🛡️ Простая обработка ошибок** — проверка статусов HTTP
- **📁 Автоматическое именование** — не нужно придумывать имена файлам
- **🔧 Расширяемость** — легко добавить поддержку других форматов

#### ❌ Недостатки
- **🎯 Узкая специализация** — работает только с тегом `<img>` в HTML
- **🖼️ Только JPG** — все изображения сохраняются с расширением `.jpg` (даже если оригинал PNG)
- **🐌 Последовательная загрузка** — изображения скачиваются по одному (можно ускорить через threading)
- **🔍 Примитивный парсинг** — используется регулярное выражение вместо полноценного HTML-парсера (BeautifulSoup)
- **🚫 Нет обработки относительных ссылок** — если ссылки не полные, могут не загрузиться

---

### 🔮 Планы по развитию

- [ ] **Поддержка BeautifulSoup** — более надёжный парсинг HTML
- [ ] **Многопоточная загрузка** — ускорение скачивания через `threading`
- [ ] **Определение формата** — сохранение с правильным расширением (jpg/png/webp)
- [ ] **Прогресс-бар** — визуальный индикатор загрузки
- [ ] **Обработка относительных ссылок** — преобразование в абсолютные
- [ ] **Поддержка аргументов командной строки** — запуск без интерактивного ввода
- [ ] **Сохранение в подпапки** — структурирование по типам контента
- [ ] **Логирование** — запись процесса в файл для отладки

---

### 🐛 Известные проблемы

| Проблема | Описание | Статус |
|----------|----------|--------|
| Неверное расширение | Все файлы сохраняются как `.jpg`, даже если оригинал PNG | Будет исправлено |
| Сайты с защитой | Некоторые ресурсы блокируют парсеры (403 Forbidden) | Требуется User-Agent |
| Относительные ссылки | Ссылки вида `/image.jpg` не загружаются | Требуется нормализация |
| Нет таймаутов | При медленном интернете может зависнуть | Добавить timeout |

---

### 📜 Лицензия

Проект распространяется под лицензией **MIT**.

**Основные положения:**
- ✅ Свободное использование и распространение
- ✅ Модификация и улучшение
- ✅ Использование в коммерческих проектах
- ❌ Нет гарантий и ответственности

---

### 👨‍💻 Для разработчиков

Вся техническая документация, детальное описание методов, планы по расширению и разбор кода находится в отдельном файле:

➡️ **[DEVELOPER.md](DEVELOPER.md)** — для разработчиков и тех, кто хочет разобраться в устройстве проекта

Там вы найдёте:
- Полное описание всех методов класса `Parser`
- Детальный разбор регулярного выражения для поиска изображений
- Пошаговое объяснение логики работы
- Примеры расширения функциональности

---

<div align="center">

**Сделано в учебных целях для изучения Python и ООП** 🐍

*Если вам помог этот проект или вы нашли ошибку — создайте Issue на GitHub!*

[⬆ Наверх](#-telegram-parser--парсер-telegram-публикаций)

</div>

---

## 🇬🇧 English version

### 🚀 Project Launch

#### Local launch
```bash
# Clone the repository
git clone https://github.com/your-username/telegram-parser.git

# Go to the project folder
cd telegram-parser

# Install the only dependency
pip install requests

# Run the parser
python parser.py
```

#### Requirements
- Python 3.x
- Library: `requests` (only dependency)
- Internet connection

---

### 📝 Project Description

**Telegram Parser** is a simple tool for downloading all images from publications on Telegra.ph (and similar websites). The project was created for educational purposes to practice:

- **Classes in Python** — encapsulating parsing logic
- **Regular expressions** — finding image links
- **HTTP requests** — downloading HTML pages and images
- **File system operations** — creating folders and saving files

---

### ✨ Key Features

| Category | Feature | Description |
|----------|---------|-------------|
| 🌐 **Parsing** | HTML download | Fetches page source code |
| | Image search | Automatically extracts all image links |
| | Regular expressions | Pattern matching `<img src="...">` |
| 💾 **Saving** | Automatic naming | Creates folder with specified or auto name |
| | Batch download | Downloads all found images |
| | File numbering | Saves as `0.jpg`, `1.jpg`, `2.jpg`... |
| 🛡️ **Reliability** | Error handling | Checks HTTP response statuses |
| | User feedback | Detailed process output |

---

### 🎯 Why a Class?

**I'm learning Python, so I'm practicing OOP!** 🐍

Using the `Parser` class is a deliberate choice to practice object-oriented programming:

| Advantage | Implementation |
|-----------|----------------|
| **Encapsulation** | All data stored within the object instance |
| **Modularity** | Each method handles one task |
| **Reusability** | Create multiple parsers without conflicts |
| **Extensibility** | Easy to add new formats via inheritance |
| **Readability** | Logically organized code |

This is a **learning project**, so it includes concepts I want to study and practice.

---

### ⚙️ How It Works

```
1. User enters publication link
                ↓
2. Parser object created
                ↓
3. download() method called
                ↓
4. Folder created for saving
                ↓
5. page() — downloads HTML
                ↓
6. parse() — finds all image links
                ↓
7. image(i) — downloads each image
                ↓
8. Done! All images saved
```

---

### 📁 Project Structure

```
📦 telegram-parser
├── 📄 parser.py          # Main parser file
├── 📄 README.md          # Documentation
├── 📄 DEVELOPER.md       # Technical documentation
└── 📁 my_images/         # Downloaded images folder (created on run)
    ├── 0.jpg
    ├── 1.jpg
    └── ...
```

---

### 📊 Advantages and Disadvantages

#### ✅ Advantages
- **✍️ Educational** — code written for learning, beginner-friendly
- **📦 Minimal dependencies** — only **1** library
- **🧩 Modular structure** — class broken into logical methods
- **🛡️ Simple error handling** — HTTP status checks
- **📁 Auto-naming** — no need to invent filenames
- **🔧 Extensible** — easy to add other formats

#### ❌ Disadvantages
- **🎯 Narrow specialization** — only works with `<img>` tags
- **🖼️ JPG only** — all images saved with `.jpg` extension
- **🐌 Sequential downloading** — images downloaded one by one
- **🔍 Primitive parsing** — regex instead of proper HTML parser
- **🚫 No relative URL handling** — relative links may fail

---

### 🔮 Development Plans

- [ ] **BeautifulSoup support** — more reliable HTML parsing
- [ ] **Multi-threaded download** — speed up via `threading`
- [ ] **Format detection** — save with correct extension
- [ ] **Progress bar** — visual download indicator
- [ ] **Relative URL handling** — convert to absolute URLs
- [ ] **Command line arguments** — run without interactive input
- [ ] **Logging** — record process for debugging

---

### 🐛 Known Issues

| Issue | Description | Status |
|-------|-------------|--------|
| Wrong extension | All files saved as `.jpg`, even PNG originals | To be fixed |
| Protected sites | Some resources block parsers (403) | Need User-Agent |
| Relative URLs | Links like `/image.jpg` fail | Need normalization |
| No timeouts | May hang on slow connection | Add timeout |

---

### 📜 License

This project is licensed under the **MIT License**.

**Key provisions:**
- ✅ Free use and distribution
- ✅ Modification and improvement
- ✅ Commercial use allowed
- ❌ No warranty or liability

---

### 👨‍💻 For Developers

All technical documentation, detailed method descriptions, and code analysis are in a separate file:

➡️ **[DEVELOPER.md](DEVELOPER.md)** — for developers and those who want to understand the project

There you will find:
- Complete description of all `Parser` class methods
- Detailed regex explanation for image search
- Step-by-step logic explanation
- Examples of extending functionality

---

<div align="center">

**Made for learning Python and OOP** 🐍

*If this project helped you or you found a bug — create an Issue on GitHub!*

[⬆ Back to top](#-telegram-parser--парсер-telegram-публикаций)

</div>
