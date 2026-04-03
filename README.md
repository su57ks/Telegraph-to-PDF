# 📸 Telegra.ph Image to PDF Downloader

<div align="center">

![Version](https://img.shields.io/badge/версия-1.1.0-brightgreen.svg?style=for-the-badge&labelColor=black)
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
- [🛡 Проверка форматов изображений](#-проверка-форматов-изображений)
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
- [🛡 Image Format Verification](#-image-format-verification)
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
cd Telegraph-to-PDF

# Установите зависимости
pip install requests img2pdf

# Запустите скрипт
python parser.py
```

#### Требования
- Python 3.x
- Библиотеки: `requests`, `img2pdf`
- Интернет-соединение

> **Примечание:** Скрипт предназначен для работы с публикациями на платформе Telegra.ph.

---

### 📝 Описание проекта

**Telegra.ph Image to PDF Downloader** — консольный инструмент, который:

- Скачивает HTML-страницу статьи Telegra.ph
- Находит все теги `<img>` и извлекает ссылки на изображения
- Загружает каждое изображение
- Проверяет валидность изображений по сигнатурам (magic bytes)
- Объединяет все изображения в один PDF-файл
- Автоматически очищает временные файлы

Проект написан вручную, код компактен и легко модифицируется.

---

### ✨ Ключевые возможности

| Категория | Функция | Описание |
|-----------|---------|----------|
| 🖼 **Загрузка** | Парсинг страницы | Извлекает все изображения из статьи Telegra.ph |
| | Скачивание изображений | Сохраняет картинки во временную папку |
| 🔍 **Валидация** | Проверка сигнатур | Определяет формат изображения по магическим байтам |
| | Поддержка 11 форматов | JPEG, PNG, GIF, BMP, WebP, TIFF, PSD, ICO и др. |
| 📄 **Конвертация** | Создание PDF | Объединяет изображения в один PDF-файл |
| 🧹 **Очистка** | Удаление кэша | Автоматически удаляет временные файлы |
| 🛡 **Обработка ошибок** | Прерывание | При Ctrl+C корректно очищает временные файлы |

---

### 🔧 Как это работает

1. Пользователь вводит ссылку на статью Telegra.ph
2. Скрипт проверяет, что ссылка принадлежит домену `telegra.ph`
3. Загружается HTML-страница
4. С помощью регулярного выражения извлекаются все значения атрибутов `src` тегов `<img>`
5. Для каждой найденной ссылки скачивается изображение
6. Запускается проверка сигнатуры изображения — файл анализируется по первым байтам
7. Если формат распознан, изображение сохраняется во временную папку
8. Все сохранённые изображения передаются в библиотеку `img2pdf`, которая создаёт PDF
9. Временная папка удаляется

#### Пример работы
```
Пожалуйста, введите ссылку на ресурс: https://telegra.ph/Пример-статьи-01-01
Пожалуйста, введите имя для папки сохранения (Enter для автоматического названия): моя_статья
HTML страница успешно скачана
Найдено 5 изображений
Скачивание изображения №1
    Картинка успешно скачана и сохранена как '0.jpg'
Скачивание изображения №2
    Картинка успешно скачана и сохранена как '1.jpg'
...
Сохранено в файл моя_статья.pdf
Удаляем файлы кэша
Кэш успешно удалён
```

---

### 🛡 Проверка форматов изображений

Функция `verify()` проверяет валидность изображения по его сигнатуре (magic bytes) — уникальной последовательности байтов в начале файла.

#### Поддерживаемые форматы и их сигнатуры:

| Формат | Сигнатура (hex) | Сигнатура (текст) |
|--------|-----------------|-------------------|
| JPEG | `FF D8` | `ÿØ` |
| PNG | `89 50 4E 47 0D 0A 1A 0A` | `‰PNG␍␊␚␊` |
| GIF87a | `47 49 46 38 37 61` | `GIF87a` |
| GIF89a | `47 49 46 38 39 61` | `GIF89a` |
| BMP | `42 4D` | `BM` |
| WebP | `52 49 46 46` | `RIFF` |
| TIFF (little-endian) | `49 49 2A 00` | `II*␀` |
| TIFF (big-endian) | `4D 4D 00 2A` | `MM␀*` |
| PSD | `38 42 50 53 00 01` | `8BPS␀␁` |
| ICO | `00 00 01 00` | `␀␀␁␀` |
| CUR | `00 00 02 00` | `␀␀␂␀` |

> **Преимущество:** Скрипт не полагается на расширение файла или Content-Type из HTTP-заголовков — только на реальное содержимое.

---

### 📊 Достоинства и недостатки

#### ✅ Достоинства
- **✍️ Написано человеком** — код прозрачен и легко читается
- **📦 Минимум зависимостей** — только `requests` и `img2pdf`
- **🖼 Надёжная валидация** — проверка по сигнатурам 11 форматов
- **🧹 Автоочистка** — не оставляет мусора на диске
- **🛡 Обработка прерывания** — корректно завершает работу при Ctrl+C

#### ❌ Недостатки
- **🎯 Только Telegra.ph** — не работает с другими сайтами без доработки
- **🐌 Нет JavaScript** — не поддерживает динамически подгружаемый контент

---

### 📜 Лицензия

Проект распространяется под лицензией **GNU General Public License v3 (GPLv3)**.

**Основные положения:**
- ✅ Свободное использование и распространение
- ✅ Доступ к исходному коду
- ✅ Модификация и улучшение
- ❌ Закрытие исходного кода (производные работы также должны быть открыты)

Полный текст лицензии доступен в файле [LICENSE](LICENSE) или на официальном сайте: https://www.gnu.org/licenses/gpl-3.0.html

---

### 👨‍💻 Для разработчиков

Подробное описание структуры кода, всех функций и форматов данных находится в отдельном файле:

➡️ **[DEVELOPER.md](DEVELOPER.md)** — для разработчиков и тех, кто хочет разобраться в устройстве проекта

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
git clone https://github.com/su57ks/Telegraph-to-PDF.git
cd Telegraph-to-PDF

# Install dependencies
pip install requests img2pdf

# Run the script
python parser.py
```

#### Requirements
- Python 3.x
- Libraries: `requests`, `img2pdf`
- Internet connection

> **Note:** The script is designed for Telegra.ph publications.

---

### 📝 Project Description

**Telegra.ph Image to PDF Downloader** is a console tool that:

- Downloads the HTML page of a Telegra.ph article
- Finds all `<img>` tags and extracts image links
- Downloads each image
- Verifies images by their signatures (magic bytes)
- Combines all images into a single PDF file
- Automatically cleans up temporary files

The code is compact and easy to modify.

---

### ✨ Key Features

| Category | Feature | Description |
|----------|---------|-------------|
| 🖼 **Download** | Page parsing | Extracts all images from a Telegra.ph article |
| | Image downloading | Saves pictures to a temporary folder |
| 🔍 **Validation** | Signature check | Identifies image format by magic bytes |
| | 11 formats supported | JPEG, PNG, GIF, BMP, WebP, TIFF, PSD, ICO, etc. |
| 📄 **Conversion** | PDF creation | Combines images into one PDF file |
| 🧹 **Cleanup** | Cache removal | Automatically deletes temporary files |
| 🛡 **Error handling** | Interruption | On Ctrl+C, correctly cleans up temporary files |

---

### 🔧 How It Works

1. User enters a Telegra.ph article link
2. The script checks that the link belongs to `telegra.ph`
3. The HTML page is downloaded
4. Using a regular expression, all `src` attribute values of `<img>` tags are extracted
5. For each found link, the image is downloaded
6. The image signature is checked using the first few bytes
7. If the format is recognized, the image is saved to a temporary folder
8. All saved images are passed to `img2pdf` to create a PDF
9. The temporary folder is deleted

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

### 🛡 Image Format Verification

The `verify()` function checks image validity by its signature (magic bytes).

#### Supported formats and signatures:

| Format | Signature (hex) | Signature (text) |
|--------|-----------------|------------------|
| JPEG | `FF D8` | `ÿØ` |
| PNG | `89 50 4E 47 0D 0A 1A 0A` | `‰PNG␍␊␚␊` |
| GIF87a | `47 49 46 38 37 61` | `GIF87a` |
| GIF89a | `47 49 46 38 39 61` | `GIF89a` |
| BMP | `42 4D` | `BM` |
| WebP | `52 49 46 46` | `RIFF` |
| TIFF (little-endian) | `49 49 2A 00` | `II*␀` |
| TIFF (big-endian) | `4D 4D 00 2A` | `MM␀*` |
| PSD | `38 42 50 53 00 01` | `8BPS␀␁` |
| ICO | `00 00 01 00` | `␀␀␁␀` |
| CUR | `00 00 02 00` | `␀␀␂␀` |

> **Advantage:** The script does not rely on file extensions or HTTP Content-Type headers — only on actual file content.

---

### 📊 Advantages and Disadvantages

#### ✅ Advantages
- **✍️ Human-written** — code is transparent and easy to read
- **📦 Minimal dependencies** — only `requests` and `img2pdf`
- **🖼 Reliable validation** — signature checking for 11 formats
- **🧹 Auto-cleanup** — leaves no garbage on disk
- **🛡 Interruption handling** — correctly exits on Ctrl+C

#### ❌ Disadvantages
- **🎯 Telegra.ph only** — does not work with other sites without modification
- **🐌 No JavaScript** — does not support dynamically loaded content

---

### 📜 License

This project is distributed under the **GNU General Public License v3 (GPLv3)**.

**Key provisions:**
- ✅ Free use and distribution
- ✅ Access to source code
- ✅ Modification and improvement
- ❌ Closing the source code (derivative works must also be open source)

The full license text is available in the [LICENSE](LICENSE) file or on the official website: https://www.gnu.org/licenses/gpl-3.0.html

---

### 👨‍💻 For Developers

Detailed documentation of the code structure, all functions, and data formats is available in a separate file:

➡️ **[DEVELOPER.md](DEVELOPER.md)** — for developers and those who want to understand the project's internals

---

<div align="center">

**Made with soul for those who save favorite articles** 💗

*If you like the project — give it a star on GitHub! ⭐*

[⬆ Back to top](#-telegraph-image-to-pdf-downloader)

</div>
```
