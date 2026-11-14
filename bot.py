import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "9196167319:AAEXGZ5Co1VH2UvSZWT-jcATLRk6aXnSwUU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
from aiohttp import web
import asyncio

async handle(request):
    return web.Response(text="Бот в сети!")

async def start_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCSite(runner, '0.0.0.0', 10000)
    await site.start()
