from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import telebot 
from telebot import types
import threading

devices = AudioUtilities.GetSpeakers()

bot = telebot.TeleBot('10000000000:AAAAAAAAAAA_BBBBBBBB-Y-ZZZZZZZZZZZZZZ') #вставить токен бота

markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
markup.row('Тише')
markup.row('Выкл звук')
markup.row('Вкл звук')

@bot.message_handler(commands=['start'])
def handle_start(message):
	bot.send_message(message.chat.id, "Жду команд", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
	if message.text.lower()=='тише': 
		while True:
			try:
				interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
				volume = cast(interface, POINTER(IAudioEndpointVolume))
				volume.SetMasterVolumeLevel(-20.0, None)
				break
			except: pass
	elif message.text.lower()=='выкл звук': 
		while True:
			try:
				interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
				volume = cast(interface, POINTER(IAudioEndpointVolume))
				volume.SetMute(1, None)
				break
			except: pass
	elif message.text.lower()=='вкл звук': 
		while True:
			try:
				interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
				volume = cast(interface, POINTER(IAudioEndpointVolume))
				volume.SetMute(0, None)
				break
			except: pass

threading.Thread(target=bot.polling).start()