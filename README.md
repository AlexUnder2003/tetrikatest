# Задания
Все решения заданий лежат в одноименных файлах, задание 2 выполнено с помощью Scrapy и находится в папке task2. Инструкция по запуску ниже.

# Task2
1. Быстрый старт (Scrapy — сбор животных по алфавиту)
Требования: Python 3.9+, pip, virtualenv (желательно)
Проверено на macOS / Linux. Для Windows команды аналогичны.
## 1. Клонируем репозиторий и заходим в директорию проекта
git clone https://github.com/AlexUnder2003/tetrikatest.git
cd task2

## 2. Создаём и активируем виртуальное окружение
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

## 3. Ставим зависимости
pip install -r requirements.txt


## 4. Запуск паука
scrapy crawl animals
В результате появится файл beasts.csv в корне проекта:

```
А,642
Б,412
В,371
```

Замечание. Wikipedia запрещает обход каталога /w/ в robots.txt.
Поэтому в спайдере стоит ROBOTSTXT_OBEY = False.