from vkbottle import Bot, Message

bot = Bot('token', 1, debug=True, plugin_folder='examplebot')

# Answer <Твой возраст ± AGE*365 дней> to <!меня зовут AGE>
@bot.on.message('!мне <age:int> лет', lower=True)
async def wrapper(ans: Message, age):
    await ans(f'Твой возраст ± {age*365} дней')

bot.run_polling()
