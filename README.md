# Асинхронный парсер PEP

Парсер документов PEP на базе фреймворка Scrapy.

## Описание

- Собирает номер, название и статус всех PEP.
- Подсчитывает общее количество каждого статуса, а также общую сумму всех статусов.

Парсер собирает данные с сайта ```https://www.python.org/```

Вся собранная информация сохраняется в файлах ```csv``` в папке ```results/...```

## Как запустить проект


Создайте виртуальное окружение:

```python
python -m venv venv
```

Активируйте виртуальное окружение:

```python
source venv/bin/activate
```

```python
pip install -r requirements.txt
```

Запустите  в консоле:

```python
scrapy crawl pep
```


Парсер добавит два файла в папку results

Файл pep_<дата><время>.csv будет содержать информацию по статьям pep

Файл status_summary_<дата><время>.csv будет содержать статистику по статусам стандартов pep

Автор: Владислав Сизов
