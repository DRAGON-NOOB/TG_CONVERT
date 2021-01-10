from pyrogram import CallbackQuery
import pyrogram

@pyrogram.Client.on_callback_query()
async def button(bot, update):
    if "start" in cb_data:
        await update.message.delete()
        await start_user(bot, update.message)
    elif "help_btn" in cb_data:
        await update.message.delete()
        await help_user(bot, update.message)
    elif "cancel_btn" in cb_data:
        await update.message.delete()
    elif "upgrade_btn" in cb_data:
        await update.message.delete()
        await upgrade(bot, update.message)
    elif "about_btn" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
