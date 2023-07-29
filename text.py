import os

HELP = 'Команды:\n/all - Тэг всех участников чата\n/settings - Настройки доступа\n/start - Приветствие\n/help - Команды'
START = 'Перед использованием пригласите бота в групповой чат, используя тег бота, и напишите /all, чтобы упомянуть всех участников.\nДля того чтобы посмотреть остальные команды пропишите /help'
SETTINGS = 'Вы можете указать, кто можеть использовать команду /all:\n/everyone - Все\n/onlyadmins - Только Администраторы'
NOT_ALLOWED = 'Эту команду могут использовать только Администраторы'
TO_SETTINGS = 'Чтобы изменить настройки доступа, администратор чата должен прописать /settings'
START_SETTING = 'Начальная настройка прошла успешно, пропишите /all еще раз'
UNKNOWN_ERROR = f'Неизвестная ошибка. Возможно, вы используете бота не в групповом, а в одиночном чате или канале. Если это так, то перед использованием пригласите бота в групповой чат, используя тег @SomethinDifferentBot. Если это не так обратитесь к {os.environ.get("OWNER")}'
ALLOW_ALL = {
	'1': 'Теперь все в этом чате могут использовать команду /all',
	'0': 'Теперь только Администраторы могут использовать команду /all'
}