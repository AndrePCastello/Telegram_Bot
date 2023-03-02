from asyncio import run
from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters    

load_dotenv()

app = Client(
    'Lojas_SP',
    api_id = getenv('TELEGRAM_ID'), 
    api_hash = getenv('TELEGRAM_HASH'), 
    bot_token = getenv('TELEGRAM_TOKEN') 
)

@app.on_message(filters.command(['start', 'menu']))
async def menu (Client, message):
    await app.send_message(message.chat.id, 'Seja Bem-Vindo!')
    await app.send_message(message.chat.id, '- Menu \n /Roupas - Para pedir o catálogo \n /tenis - Para acessar os nossos tênis \n'
    '/Shorts - Para acessar os shorts')

@app.on_message(filters.command('Roupas'))
async def roupas(Client, message):
    await app.send_message(message.chat.id, '- Roupas \n /Moleton \n /Blusas')

@app.on_message(filters.command('Moleton'))
async def moleton(Client, message):
    await message.reply_photo('https://images.pexels.com/photos/1082528/pexels-photo-1082528.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
    await app.send_message(message.chat.id, '$20,00')
    await app.send_message(message.chat.id, '/menu')

@app.on_message(filters.command('Blusas'))
async def blusas(Client, message):
    await message.reply_photo('https://images.pexels.com/photos/10330179/pexels-photo-10330179.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
    await app.send_message(message.chat.id, '$50,00 \n /menu')

@app.on_message(filters.command('shorts'))
async def shorts(Client, message):
    await app.send_message(message.chat.id, '- Shorts \n /Praia \n /Esporte')

@app.on_message(filters.command('Praia'))
async def praia(Client, message):
    await app.send_photo(message.chat.id, 'https://images.pexels.com/photos/14406486/pexels-photo-14406486.jpeg?auto=compress&cs=tinysrgb&w=600')
    await app.send_message(message.chat.id, '$20')
    await app.send_message(message.chat.id, '/menu')

@app.on_message(filters.command('Esporte'))
async def esporte(Client, message):
    await app.send_photo(message.chat.id, 'https://images.pexels.com/photos/13673630/pexels-photo-13673630.jpeg?auto=compress&cs=tinysrgb&w=600')
    await app.send_message(message.chat.id, '$50')
    await app.send_message(message.chat.id, '/menu')

@app.on_message(filters.command('tenis'))
async def tênis(Client, message):
    await app.send_message(message.chat.id, '- Tenis \n /nike \n /puma')

@app.on_message(filters.command('nike'))
async def nike(Client, message):
    await message.reply_photo('https://images.pexels.com/photos/1598505/pexels-photo-1598505.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
    await app.send_message(message.chat.id, '$100,00 \n /menu')

@app.on_message(filters.command('puma'))
async def puma(Client, message):
    await message.reply_photo('https://images.pexels.com/photos/6719186/pexels-photo-6719186.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
    await app.send_message(message.chat.id, '$200,00 \n /menu')

print('iniciou')
app.run()

# send_message serve para enviar uma mensagem, assim como send_photo, que serve para enviar uma foto.
# O "Await" serve para esperar entre os usuários para assim mandar o que lhe foi pedido.
# app é o nome de meu algoritmo, ou o nome do meu sistema, neste caso pode-se escolhido qualquer outro nome no lugar.
# app.run serve para mandar o sistema iniciar, run = "correr."
# Na parte de "App.Client estão as minhas informações de verificação/login da api do telegram."
# load dotenv carrega os meus arquivos .env