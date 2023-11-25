# tg-tag-all-bot

## Usage
1. Set up environment variables on your machine (Docker will use them automaticly). Example:
```
OWNER_TAG = @tg_tag
BOT_TOKEN = 9874972487:FDSADFsdlakflsdfDSfasd
API_ID = 90833402
API_HASH = alkdsjf879afukjef29f2uakjsf
```
2. Run
```docker-compose -f "docker-compose.yaml" up --build --force-recreate -d```
3. How to use it in telegram:
Перед использованием пригласите бота в групповой чат, используя тег бота, и напишите /all, чтобы упомянуть всех участников. Для того чтобы посмотреть остальные команды пропишите /help

## Команды:

/all - Тэг всех участников чата

/settings - Настройки доступа

/start - Приветствие

/help - Команды

## TODO
-  Use secrets in docker instead of env
-  Add persistent database
-  Translate everything to english (README.md and text.py)
