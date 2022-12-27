# from progress.bar import Bar

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     bar.next()
# bar.finish()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5856713148:AAHrdpFripCPdJaoRt_RoBKNct-_t3Ztr94").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print("Server start")

app.run_polling()
