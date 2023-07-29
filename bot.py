import configparser
import logging
import os
from text import *
from telethon.sync import TelegramClient, events

os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/bot.log', level=logging.INFO)

config = configparser.ConfigParser()
config.read('config.ini')
BotConf = config['Bot']

TOKEN = os.environ.get('BOT_TOKEN')
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token = TOKEN)


async def UnknownError(bot, chat):
	logging.error(f"Unknown error occurred in chat {chat.id}")
	await bot.send_message(chat, UNKNOWN_ERROR)

async def check_admin(bot, chat, sender, num):
	if (await bot.get_permissions(chat, sender)).is_admin:
		return True
	elif num:
		logging.warning(f"User {sender.id} tried to perform an admin action in chat {chat.id} without permission")
		await bot.send_message(chat, NOT_ALLOWED)
		return False

async def change_settings(num, bot, chat, sender):
	if await check_admin(bot, chat, sender, 1):
		await bot.send_message(chat, ALLOW_ALL[num])
		BotConf[f'{chat.id}'] = num
		with open('config.ini', 'w') as configfile:
			config.write(configfile)
		logging.info(f"Settings changed to {num} in chat {chat.id} by user {sender.id}")


@bot.on(events.NewMessage)
async def handler(message):
	chat = await message.get_chat()
	sender = await message.get_sender()

	try:
		if 'start' in message.raw_text:
			await bot.send_message(chat, START)
			logging.info(f"Bot started in chat {chat.id}")
			return

		elif 'help' in message.raw_text:
			await bot.send_message(chat, HELP)
			logging.info(f"Help message sent to chat {chat.id}")
			return

		elif 'settings' in message.raw_text:
			if await check_admin(bot, chat, sender, 1):
				await bot.send_message(chat, SETTINGS)
				logging.info(f"Settings requested in chat {chat.id} by user {sender.id}")
			return

		elif 'everyone' in message.raw_text:
			await change_settings('1', bot, chat, sender)
			return

		elif 'onlyadmins' in message.raw_text:
			await change_settings('0', bot, chat, sender)
			return

		elif 'all' in message.raw_text:
			perm = int(BotConf[f'{chat.id}'])
			if perm or not perm and await check_admin(bot, chat, sender, 0):
				sendername = f'{sender.first_name} {sender.last_name}'
				if sender.username:
					sendername += f' ({sender.username}) '
				users = await bot.get_participants(chat)
				usernames = []
				ids = []
				for user in users:
					if not user.bot:
						ids.append(user.id)
						usernames.append(user.first_name)
				who_ment = f'{sendername} упомянул всех участников'
				ments = ''.join(f'[⠀](tg://user?id={ids[i]})' for i in range(len(ids)))
				await bot.send_message(chat, who_ment + ments)
				logging.info(f"All users mentioned in chat {chat.id} by user {sender.id}")
			else:
				await bot.send_message(chat, f'{NOT_ALLOWED}\n{TO_SETTINGS}')
				logging.warning(f"User {sender.id} tried to mention all users in chat {chat.id} without permission")
			return
	except KeyError:
		try:
			BotConf[f'{chat.id}'] = '0'
			with open('config.ini', 'w') as configfile:
				config.write(configfile)
			await bot.send_message(chat, START_SETTING)
			logging.info(f"Bot started in chat {chat.id}")
		except:
			await UnknownError(bot, chat)
	except:
		await UnknownError(bot, chat)

if __name__ == '__main__':
	bot.start()
	bot.run_until_disconnected()