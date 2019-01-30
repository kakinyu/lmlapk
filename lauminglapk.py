from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer;
import telepot
from telepot.loop import MessageLoop
import time

model = joblib.load("model.pkl")

def prediction(content):
    predictions = model.predict_proba([content])
    predictions = str(predictions[0])
    predictions = predictions.replace("["," ");
    predictions = predictions.replace("]"," ");
    neg, pos = predictions.split(" ")
    pos = float(pos)
    neg = float(neg)
    if(pos >= neg):
        result = "This is a positive review! "+"( "+"{0:.2f}".format(pos)+")";
    else:
        result = "This is a negative review! "+"( "+"{0:.2f}".format(pos)+")";
    return result

def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg);

    if content_type == "text":
        content = msg["text"];
        predictResult = prediction(content);
        bot.sendMessage(chat_id, predictResult);

if __name__ == "__main__":
    
    bot = telepot.Bot("661014557:AAFVFNDAqdiNEyv2gj-CwI7arxZN8DiTZ94");
    MessageLoop(bot, handle).run_as_thread();

    while True:
        time.sleep(10)


