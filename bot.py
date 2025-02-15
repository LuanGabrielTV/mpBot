from os import path
from config import API_TOKEN, WHITE_LIST

from telebot import types, TeleBot
from downloader import get_audio_from_video, download_reel_video
from constants import callback_data_video, callback_data_audio, \
            download_path, default_video_name, default_audio_name, \
            separator

bot = TeleBot(API_TOKEN)
    
@bot.callback_query_handler(func=lambda callback: True)
def answer(callback):
    if callback.message:
        if callback.data == callback_data_video:
            with open(path.join(download_path, default_video_name), 'rb') as video:
                bot.send_video(callback.message.chat.id, video)
        if callback.data == callback_data_audio:
            get_audio_from_video()
            with open(path.join(download_path, default_audio_name), 'rb') as audio:
                bot.send_audio(callback.message.chat.id, audio)
            
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Bem vindo(a)! Envie um link.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.from_user.id in WHITE_LIST:
        reel_id = (message.text)[31:].split(separator, 1)[0]
        
        markup = types.InlineKeyboardMarkup(row_width=2)
        
        is_video_button = types.InlineKeyboardButton('Video', callback_data=callback_data_video)    
        is_audio_button = types.InlineKeyboardButton('Audio', callback_data=callback_data_audio)    
        
        markup.add(is_video_button, is_audio_button)
        
        try:
            download_reel_video(reel_id)
            bot.send_message(message.chat.id, 'O que você deseja baixar?', reply_markup=markup)
        except:
            bot.reply_to(message, 'Não foi possível baixar o vídeo. Tente outra url.')

def main():
    bot.polling()
    
if __name__ == '__main__':
    main() 

