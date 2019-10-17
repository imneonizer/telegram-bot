from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import imcrypt

token = imcrypt.decrypt('yaf4vmenfcVDhDp2F4a78bmzZHYGd2WCZOgy52njY1GnYttDLEv+huentcWKEm6A')
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    username = update.message.chat.username
    first_name = update.message.chat.first_name
    chat_id = update.effective_chat.id
    reply = f"Hi! {first_name} i am your Earn Together buddy,\nyour id is {update.effective_chat.id}"
    context.bot.send_message(chat_id=chat_id, text=reply)
dispatcher.add_handler(CommandHandler('start', start))


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
dispatcher.add_handler(MessageHandler(Filters.text, echo))


def login(update, context):
    username = update.message.chat.username
    password = context.args[0]
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"username: {username}\npasword: {password}")
dispatcher.add_handler(CommandHandler('login', login))


def game(update, context):
    keyboard = [[InlineKeyboardButton("1. odd-even", callback_data='odd-even')],
                [InlineKeyboardButton("2. simple-math", callback_data='simple-math')],
                [InlineKeyboardButton("3. large-small", callback_data='large-small')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('choose a game', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    query.edit_message_text(text="ok lets play {}".format(query.data))

updater.dispatcher.add_handler(CommandHandler('game', game))
updater.dispatcher.add_handler(CallbackQueryHandler(button))


#launch the bot#########
updater.start_polling()
#######################