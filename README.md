# Скачивание фото связанные с космосом
данная программа скачивает фото из таких источников как NASA и Spacex и отправляет их ботом в телеграмм.

### Как установить
Для работы с NASA сгенерируйте API ключ на сайте [NASA](https://api.nasa.gov/).
Храните ключ в переменной "API_NASA_KEY" в  созданном .env файле.
```
API_NASA_KEY="ваш ключ"
```
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```


### Как запустить
для запуска скачивания фоток дня от NASA следует ввести в терминал:
```
python downloads_nasa_apod.py 
```
следует указать ключ "count" - количество фото.
```
python downloads_nasa_apod.py --count количество фото
```


для запуска скачивания фото от spacex следует ввести в терминал:
```
python fetch_spacex_images.py
```
указать свой id в ключе "id"
```
python fetch_spacex_images.py --id id запуска
```


для запуска скачивания фото Земли следует ввести в терминал:
```
python get_epic_images.py
```


для запуска бота следует ввести в терминал:
```
python python-telegram-bot.py
```
указать ключ "delay" - задержка между отправкой всех фото и ключ "chat_id" - ваш чат id.
```
python python-telegram-bot.py --delay время в секундах --chat_id "ваш чат id"
```

### Цели проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).