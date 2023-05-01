


import requests
import logging


from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5970622317:AAFgQsKj4nQ7MjSSsO2CDQEAq_w80L3YIDI'



logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
 
    await message.reply("Assalomu aleykum ushbu bot 5 ta tilga tarjima qiladi  .")


@dp.message_handler()
async def echo(message: types.Message):
    xabar=message.text
    r =  requests.get(f'https://trans.noxi8.repl.co/ru/text={xabar}')
    r2 = requests.get(f'https://trans.noxi8.repl.co/en/text={xabar}')
    r3 = requests.get(f'https://trans.noxi8.repl.co/fr/text={xabar}')
    r4 = requests.get(f'https://trans.noxi8.repl.co/ar/text={xabar}')
    r5 = requests.get(f'https://trans.noxi8.repl.co/tr/text={xabar}')
    response =  r.json()['text']
    response2 = r2.json()['text']
    response3 = r3.json()['text']
    response4 = r4.json()['text']
    response5 = r5.json()['text']
    await message.reply(f'rus tilidagi tarjimasi:{response}\nIngiliz tilidagi tarjimasi:{response2}\nFransuz tiliga tarjimasi{response3}\nArab tiliga tarjimasi{response4}\nTurk tiliga tarjimasi{response5}')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
