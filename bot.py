import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Inisialisasi logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Token bot Telegram (ganti dengan token bot Anda)
TOKEN = "6809318416:AAH0tLqUZ4CH9QAJ8O1i_eqqiCvXNjqo3s4"

# Daftar alamat IP yang diizinkan (kosongkan awalnya)
allowed_ips = []

# Fungsi untuk menambahkan alamat IP ke daftar
def add_ip(update: Update, context: CallbackContext) -> None:
    global allowed_ips
    # Mendapatkan alamat IP dari pesan pengguna
    ip_address = update.message.text.split()[1]
    # Menambahkan alamat IP ke daftar jika belum ada
    if ip_address not in allowed_ips:
        allowed_ips.append(ip_address)
        update.message.reply_text(f"Alamat IP {ip_address} telah ditambahkan ke daftar.")
    else:
        update.message.reply_text(f"Alamat IP {ip_address} sudah ada dalam daftar.")

# Fungsi untuk mendapatkan daftar alamat IP
def get_ips(update: Update, context: CallbackContext) -> None:
    global allowed_ips
    update.message.reply_text("Daftar Alamat IP yang Diizinkan:\n" + "\n".join(allowed_ips))

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # Menambahkan handler untuk perintah '/addip'
    dispatcher.add_handler(CommandHandler("addip", add_ip))

    # Menambahkan handler untuk perintah '/getips'
    dispatcher.add_handler(CommandHandler("getips", get_ips))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
