from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes):
    await log(update, context)
    await update.message.reply_text(f'/Hello\n/time\n/help\n')

async def time_command(update: Update, context: ContextTypes):
    await log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes):
    await log(update, context)
    msg = update.message.text
    items = msg.split()  # sum num1 num2
    x_1 = int(items[1])
    x_2 = int(items[2])
    await update.message.reply_text(f'{x_1} + {x_2} = {x_1+x_2}')