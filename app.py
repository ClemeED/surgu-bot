import os
import threading
from flask import Flask
import bot

app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health():
    return "Bot is running", 200

if __name__ == "__main__":
    bot_thread = threading.Thread(target=lambda: bot.bot.polling(none_stop=True, timeout=60, long_polling_timeout=60))
    bot_thread.daemon = True
    bot_thread.start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)