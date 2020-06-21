import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
debtdict = {}

def start(update, context):
    update.message.reply_text('Прив')
    if  update.message.chat_id not in debtdict:
        debtdict[update.message.chat_id ] = {}
    update.message.reply_text('Доступные команды: \n'
    '/debt name sum \n'
    '/all_debts')

def debt(update, context):
    s = update.message.text.split()
    if s[1] in debtdict[update.message.chat_id]:
        debtdict[update.message.chat_id][s[1]] += int(s[2])
    else:
        debtdict[update.message.chat_id][s[1]] = int(s[2])
    update.message.reply_text('Долг %s обновлен.'%s[1])
def all_debts(update, context):
    s=''
    update.message.reply_text('Список должников')
    for k, a in debtdict[update.message.chat_id ].items(): 
        s += str(k) +' '+ str(a)+'\n'
    update.message.reply_text(s)



def main():
    updater = Updater('1240679891:AAFvlcQ5imdSsdEoKNZUjdsuzOLAW_CYxxw',use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('debt', debt))
    dp.add_handler(CommandHandler('all_debts', all_debts))
   
    updater.start_polling()
    updater.idle()
if __name__== '__main__':
    main()
    print (debtdict)