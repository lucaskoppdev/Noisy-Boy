from telegram import Update
from telegram.ext import Application, MessageHandler, filters
from main import main_function


async def send_response(update: Update, context):
    user_input = update.message.text
    
    print(f"O usuario digitou: {user_input}")
    resposta = main_function(user_input)
    await update.message.reply_text(resposta)


app = Application.builder().token("8351546507:AAHTMW0yuokh-awtElae6bk3F2i35sy3Xvs").build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_response))

print("passou aqui, ta rodando!")
app.run_polling()
