# tg-tag-all-bot

## Usage
1. Set up .env. Example:
```
OWNER_TAG = @tg_tag
BOT_TOKEN = 9874972487:FDSADFsdlakflsdfDSfasd
API_ID = 90833402
API_HASH = alkdsjf879afukjef29f2uakjsf
```
2. Run
```docker-compose -f "docker-compose.yaml" up --build --force-recreate -d```
3. How to use it in tg:
Перед использованием пригласите бота в групповой чат, используя тег бота, и напишите /all, чтобы упомянуть всех участников. Для того чтобы посмотреть остальные команды пропишите /help

## Команды:

/all - Тэг всех участников чата

/settings - Настройки доступа

/start - Приветствие

/help - Команды

## TODO
-  Translate everything to english (README.md and text.py)
