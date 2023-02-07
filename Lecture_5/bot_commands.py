from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')
    
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'Time = {datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'/hi\n/time\n/help')
    
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    x1 = int(items[1])
    x2 = int(items[2])
    await update.message.reply_text(f'{x1} + {x2} = {x1+x2}')