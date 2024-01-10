from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
import asyncio

# to add new bot:
# git clone https://github.com/andykras/gptbot.git bot3
import bot1, bot2  #, bot3, ...

tokens = [
    bot1.env.BOT_TOKEN,
    bot2.env.BOT_TOKEN,
]

routers = [
    bot1.handlers.router,
    bot2.handlers.router,
]


async def main():
  tasks = []
  for token, router in zip(tokens, routers):
    bot = Bot(token=token, parse_mode=ParseMode.MARKDOWN)
    dp = Dispatcher()
    dp.include_router(router)
    tasks.append(dp.start_polling(bot, handle_signals=False, polling_timeout=100))

  await asyncio.gather(*tasks)


try:
  asyncio.run(main())
except KeyboardInterrupt:
  print('stopped')
  pass
