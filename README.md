# 📸 Telegra.ph Image to PDF Downloader

<div align="center">

![Version](https://img.shields.io/badge/версия-1.0.0-brightgreen.svg?style=for-the-badge&labelColor=black)
![License](https://img.shields.io/badge/лицензия-GPLv3-blue.svg?style=for-the-badge&labelColor=black)
![Python](https://img.shields.io/badge/Python-3.x-3776AB.svg?style=for-the-badge&labelColor=black&logo=python)
![Console](https://img.shields.io/badge/платформа-консоль-black.svg?style=for-the-badge&labelColor=black)
![Dependencies](https://img.shields.io/badge/зависимости-2-important.svg?style=for-the-badge&labelColor=black)
![Human written](https://img.shields.io/badge/написано-человеком-ff69b4.svg?style=for-the-badge&labelColor=black)

**✨ Загрузка всех изображений из статьи Telegra.ph и объединение их в один PDF ✨**

</div>

---

## 📋 Содержание

<details>
<summary><b>🇷🇺 Русская версия</b></summary>

<br>

- [🚀 Запуск проекта](#-запуск-проекта)
- [📝 Описание проекта](#-описание-проекта)
- [✨ Ключевые возможности](#-ключевые-возможности)
- [🔧 Как это работает](#-как-это-работает)
- [📊 Достоинства и недостатки](#-достоинства-и-недостатки)
- [📜 Лицензия](#-лицензия)
- [👨‍💻 Для разработчиков](#-для-разработчиков)

</details>

<details>
<summary><b>🇬🇧 English version</b></summary>

<br>

- [🚀 Project Launch](#-project-launch)
- [📝 Project Description](#-project-description)
- [✨ Key Features](#-key-features)
- [🔧 How It Works](#-how-it-works)
- [📊 Advantages and Disadvantages](#-advantages-and-disadvantages)
- [📜 License](#-license)
- [👨‍💻 For Developers](#-for-developers)

</details>

---

## 🇷🇺 Русская версия

### 🚀 Запуск проекта

#### Локальный запуск
```bash
# Клонируйте репозиторий
git clone https://github.com/su57ks/Telegraph-to-PDF.git
cd telegraph-pdf-downloader

# Установите зависимости
pip install requests img2pdf

# Запустите скрипт
python parser.py
```

#### Требования
- Python 3.x
- Библиотеки: `requests`, `img2pdf` (автоматически устанавливаются через pip)
- Интернет-соединение

> **Примечание:** Скрипт предназначен для работы с публикациями на платформе Telegra.ph. Для других сайтов он не оптимизирован.

---

### 📝 Описание проекта

**Telegra.ph Image to PDF Downloader** — это простой консольный инструмент, который:

- Скачивает HTML-страницу статьи Telegra.ph
- Находит все теги `<img>` и извлекает ссылки на изображения
- Загружает каждое изображение (поддерживаются форматы JPEG, PNG, GIF и др.)
- Объединяет все изображения в один PDF-файл
- Автоматически очищает временные файлы

Проект написан вручную, без использования искусственного интеллекта. Весь код компактен и легко модифицируется.

---

### ✨ Ключевые возможности

| Категория | Функция | Описание |
|-----------|---------|----------|
| 🖼 **Загрузка** | Парсинг страницы | Извлекает все изображения из статьи Telegra.ph |
| | Скачивание изображений | Сохраняет картинки во временную папку |
| 📄 **Конвертация** | Создание PDF | Объединяет изображения в один PDF-файл |
| 🧹 **Очистка** | Удаление кэша | Автоматически удаляет временные файлы после завершения |
| 🛡 **Обработка ошибок** | Прерывание | При Ctrl+C корректно очищает временные файлы |

---

### 🔧 Как это работает

1. Пользователь вводит ссылку на статью Telegra.ph (например, `https://telegra.ph/Название-статьи-01-01`)
2. Скрипт проверяет, что ссылка принадлежит домену `telegra.ph`
3. Загружается HTML-страница
4. С помощью регулярного выражения извлекаются все значения атрибутов `src` тегов `<img>`
5. Для каждой найденной ссылки скачивается изображение и сохраняется во временную папку с именем папки, указанным пользователем (или автоматически сгенерированным из названия статьи)
6. Все сохранённые изображения передаются в библиотеку `img2pdf`, которая создаёт PDF-файл
7. Временная папка удаляется

#### Пример работы
```
Пожалуйста, введите ссылку на ресурс: https://telegra.ph/Пример-статьи-01-01
Пожалуйста, введите имя для папки сохранения (Enter для автоматического названия): моя_статья
HTML страница успешно скачана
Найдено 5 изображений
Скачивание изображения №1
    Картинка успешно скачана и сохранена как '0.jpg'
...
Сохранено в файл моя_статья.pdf
Удаляем файлы кэша
Кэш успешно удалён
```

---

### 📊 Достоинства и недостатки

#### ✅ Достоинства
- **✍️ Написано человеком** — код прозрачен и легко читается
- **📦 Минимум зависимостей** — только две библиотеки: `requests` и `img2pdf`
- **🖼 Поддержка любых форматов** — скачивает любые изображения, доступные по ссылкам
- **🧹 Автоочистка** — не оставляет мусора на диске
- **🛡 Обработка прерывания** — корректно завершает работу при Ctrl+C

#### ❌ Недостатки
- **🎯 Ориентирован только на Telegra.ph** — не работает с другими сайтами без доработки
- **🐌 Нет обработки динамического контента** — не поддерживает JavaScript-рендеринг
- **📄 Простая проверка формата** — проверяет только начало файла на `RIFF` (WebP), остальные форматы пропускает (это можно улучшить)

---

### 📜 Лицензия

Проект распространяется под лицензией **GNU General Public License v3 (GPLv3)**.

**Основные положения:**
- ✅ Свободное использование и распространение
- ✅ Доступ к исходному коду
- ✅ Модификация и улучшение
- ❌ Закрытие исходного кода (производные работы также должны быть открыты)
- ❌ Использование проприетарных модулей без открытия кода

Полный текст лицензии доступен в файле [LICENSE](LICENSE) или на официальном сайте: https://www.gnu.org/licenses/gpl-3.0.html

---

### 👨‍💻 Для разработчиков

#### Структура кода

Класс `Parser` содержит следующие методы:

| Метод | Описание |
|-------|----------|
| `__init__(self, pLink, pName)` | Инициализация: сохраняет ссылку, имя папки, создаёт пустые списки |
| `download(self)` | Главный метод: создаёт папку, вызывает page(), parse(), скачивает изображения, создаёт PDF, удаляет папку |
| `page(self)` | Загружает HTML-страницу по ссылке, сохраняет в self.data |
| `parse(self)` | Парсит self.data с помощью регулярного выражения, находит все img src |
| `image(self, i)` | Скачивает изображение по ссылке self.links[i], сохраняет в папку, добавляет путь в self.images |

#### Рекомендации по добавлению лицензионного заголовка

Рекомендуется добавить в начало файла `parser.py` следующий заголовок:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Telegra.ph Image to PDF Downloader
# Copyright (C) 2024  [Ваше имя или организация]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from os import mkdir
# ... остальной код
```

#### Возможные улучшения
- Добавить поддержку других сайтов через конфигурацию
- Улучшить определение формата изображений (использовать `imghdr` или `python-magic`)
- Добавить прогресс-бар для загрузки
- Реализовать выбор страниц для PDF (если нужно не всё)
- Добавить возможность указывать имя выходного PDF
- Создать файл `LICENSE` с полным текстом GPLv3

---

<div align="center">

**Сделано с душой для тех, кто сохраняет любимые статьи** 💗

*Если вам понравился проект — поставьте звезду на GitHub! ⭐*

[⬆ Наверх](#-telegraph-image-to-pdf-downloader)

</div>

---

## 🇬🇧 English version

### 🚀 Project Launch

#### Local launch
```bash
# Clone the repository
git clone https://github.com/your-repo/telegraph-pdf-downloader.git
cd telegraph-pdf-downloader

# Install dependencies
pip install requests img2pdf

# Run the script
python parser.py
```

#### Requirements
- Python 3.x
- Libraries: `requests`, `img2pdf` (installed automatically via pip)
- Internet connection

> **Note:** The script is designed to work with Telegra.ph publications. It is not optimized for other sites.

---

### 📝 Project Description

**Telegra.ph Image to PDF Downloader** is a simple console tool that:

- Downloads the HTML page of a Telegra.ph article
- Finds all `<img>` tags and extracts image links
- Downloads each image (supports JPEG, PNG, GIF, etc.)
- Combines all images into a single PDF file
- Automatically cleans up temporary files

The project is hand-written, without using artificial intelligence. The code is compact and easy to modify.

---

### ✨ Key Features

| Category | Feature | Description |
|----------|---------|-------------|
| 🖼 **Download** | Page parsing | Extracts all images from a Telegra.ph article |
| | Image downloading | Saves pictures to a temporary folder |
| 📄 **Conversion** | PDF creation | Combines images into one PDF file |
| 🧹 **Cleanup** | Cache removal | Automatically deletes temporary files after completion |
| 🛡 **Error handling** | Interruption | On Ctrl+C, correctly cleans up temporary files |

---

### 🔧 How It Works

1. User enters a Telegra.ph article link (e.g., `https://telegra.ph/Article-Title-01-01`)
2. The script checks that the link belongs to the `telegra.ph` domain
3. The HTML page is downloaded
4. Using a regular expression, all `src` attribute values of `<img>` tags are extracted
5. For each found link, the image is downloaded and saved to a temporary folder named by the user (or auto-generated from the article title)
6. All saved images are passed to the `img2pdf` library, which creates a PDF file
7. The temporary folder is deleted

#### Example Run
```
Please enter the resource link: https://telegra.ph/Example-Article-01-01
Please enter a folder name (Enter for auto): my_article
HTML page successfully downloaded
Found 5 images
Downloading image #1
    Image successfully downloaded and saved as '0.jpg'
...
Saved to file my_article.pdf
Deleting cache files
Cache successfully deleted
```

---

### 📊 Advantages and Disadvantages

#### ✅ Advantages
- **✍️ Human-written** — code is transparent and easy to read
- **📦 Minimal dependencies** — only two libraries: `requests` and `img2pdf`
- **🖼 Any format support** — downloads any images available via links
- **🧹 Auto-cleanup** — leaves no garbage on disk
- **🛡 Interruption handling** — correctly exits on Ctrl+C

#### ❌ Disadvantages
- **🎯 Only for Telegra.ph** — does not work with other sites without modification
- **🐌 No dynamic content handling** — does not support JavaScript rendering
- **📄 Simple format check** — only checks the file header for `RIFF` (WebP), other formats are skipped (can be improved)

---

### 📜 License

This project is distributed under the **GNU General Public License v3 (GPLv3)**.

**Key provisions:**
- ✅ Free use and distribution
- ✅ Access to source code
- ✅ Modification and improvement
- ❌ Closing the source code (derivative works must also be open source)
- ❌ Use of proprietary modules without opening the code

The full license text is available in the [LICENSE](LICENSE) file or on the official website: https://www.gnu.org/licenses/gpl-3.0.html

---

### 👨‍💻 For Developers

#### Code Structure

The `Parser` class contains the following methods:

| Method | Description |
|--------|-------------|
| `__init__(self, pLink, pName)` | Initialization: saves the link, folder name, creates empty lists |
| `download(self)` | Main method: creates folder, calls page(), parse(), downloads images, creates PDF, deletes folder |
| `page(self)` | Downloads the HTML page from the link, saves to self.data |
| `parse(self)` | Parses self.data with a regular expression, finds all img src |
| `image(self, i)` | Downloads the image from self.links[i], saves to folder, adds path to self.images |

#### Recommendation for Adding License Header

It is recommended to add the following header to the beginning of the `parser.py` file:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Telegra.ph Image to PDF Downloader
# Copyright (C) 2024  [Your Name or Organization]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from os import mkdir
# ... rest of the code
```

#### Possible Improvements
- Add support for other sites via configuration
- Improve image format detection (use `imghdr` or `python-magic`)
- Add a progress bar for downloads
- Implement page selection for PDF (if not all are needed)
- Add the ability to specify the output PDF name
- Create a `LICENSE` file with the full GPLv3 text

---

<div align="center">

**Made with soul for those who save favorite articles** 💗

*If you like the project — give it a star on GitHub! ⭐*

[⬆ Back to top](#-telegraph-image-to-pdf-downloader)

</div>
```
