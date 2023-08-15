# Для подключение библиотеки telebot нужно в google colab добавить: !pip install pyTelegramBotAPI
from telebot import TeleBot, types
import json

bot = TeleBot(token='6134777758:AAH5YHzN1oP70b_qL9zRjz4zPTjsPXxaORo', parse_mode='html') # создание бота


bot = TeleBot(token='6134777758:AAH5YHzN1oP70b_qL9zRjz4zPTjsPXxaORo', parse_mode='html') 



@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    
    bot.send_message(
        chat_id=message.chat.id, 
        text='Привет! Я умею проверять JSON и форматировать его в beautiful текст, смотря сколько details \nВведи JSON details в виде строки:', 
    )


@bot.message_handler()
def message_handler(message: types.Message):
    try:
        
        payload = json.loads(message.text)
    except json.JSONDecodeError as ex:
      
        bot.send_message(
            chat_id=message.chat.id,
            text=f'При обработке произошла collision:\n<code>{str(ex)}</code>'
        )
        
        return
    
    
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
   
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Теперь твой JSON very, очень очень affordable:) \n<code>{text}</code>'
    )



def main():
  
    bot.infinity_polling()


if __name__ == '__main__':
    main()