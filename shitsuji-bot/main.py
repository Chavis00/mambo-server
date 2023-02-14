from telegram.ext import Updater, CommandHandler
from functions.basics import error
from functions import basics
from settings import INSTALLED_APPS, TOKEN
from functions.torrent_downloader import Torrent_Downloader


def main():
    bot = Updater(token=TOKEN, use_context=True)

    dispatcher = bot.dispatcher

    dispatcher.add_handler(CommandHandler("start", basics.start))
    dispatcher.add_handler(CommandHandler("help", basics.help))
    if 'TORRENT' in INSTALLED_APPS:
        torrent = Torrent_Downloader()
        dispatcher.add_handler(CommandHandler("torrent", torrent.upload_torrent))

    if 'GSHEET' in INSTALLED_APPS:
        from functions.third_apps import google_sheet_API
        sheetAPI = google_sheet_API.Gsheet_Helper()
        dispatcher.add_handler(CommandHandler("spend", sheetAPI.spend))
        dispatcher.add_handler(CommandHandler("tip", sheetAPI.add_tip))
        dispatcher.add_handler(CommandHandler("total", sheetAPI.total))
        dispatcher.add_handler(CommandHandler("rm", sheetAPI.rm_last))

    if 'RECIPE' in INSTALLED_APPS:
        from functions.third_apps import recipeapi
        recetasAPI = recipeapi.RecipeAPI()
        dispatcher.add_handler(CommandHandler("recipe", recetasAPI.send_recipe))

    dispatcher.add_error_handler(error)

    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
