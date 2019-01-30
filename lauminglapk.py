import telepot
from telepot.loop import MessageLoop
import time

def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg);

    if content_type == "text":
        content = msg["text"];
        bot.sendMessage(chat_id, content);

if __name__ == "__main__":
    
    bot = telepot.Bot("661014557:AAFVFNDAqdiNEyv2gj-CwI7arxZN8DiTZ94");
    MessageLoop(bot, handle).run_as_thread();

    while True:
        time.sleep(10)


