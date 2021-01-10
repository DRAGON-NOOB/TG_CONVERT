class Translation(object):
    START_TEXT = """🚴Hello {},
This is a Telegram File convert Bot!
You can convert any Telegram Document, using this 🤖bot! With custom thumbnail /help
     
    """
    ABS_TEXT = " Please don't be selfish."
    BANNED_USER_TEXT = "you are banned"
    UPGRADE_TEXT = "No upgrade plan 🥰"
    DOWNLOAD_START = "trying to download🚀"
    UPLOAD_START = "trying to upload🛸"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "https://t.me/FileConverterV2TGBot"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nPlease rate me if you find me useful. https://t.me/tlgrmcbot?start=anydl_bot-bot \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in next 24 hr"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully⚡."
    CUSTOM_CAPTION_UL_FILE = ""
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found🚴."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: <a href='https://t.meTG_BotZ/125'>{}</a>
Expires on: {}"""
    HELP_USER = """ITz Me 💡:
👉 <a href="https://telegram.dog/FileConverterV2TGBot">Convert To Streamable video any telegram file</a>
--------

🔥 How to deploy : <a href='https://t.me/joinchat/WD5C6OsRDjHIW-zR'>Click here</a>

    © Group   : @TGB_Support
    © Channel : @TG_BotZ 
    © credits : @rosebakthan
    Hei Follow These Steps

1. Send A Telegram Media To Convert
2. Send Custom Thumbnail
3. Replay to a Telegram Media /converttovideo Or /converttofile

Features

  >>> 
Convert any Telegram Document to Streaming Video
  >>> 
Convert any Streaming Video to Telegram Document
  >>> 
Custom thumbnail Support

Available Commands

/converttovideo -
Use This Command To Get Streamable Video
/converttofile -
Use this Command To Get Document File
/deletethumbnail -
Delete Your Saved Thumbnail

Send /me to know current plan details
keyboard = [[InlineKeyboardButton(text="💻Support Group", url="https://t.me/TGB_Support"),
                InlineKeyboardButton(text="🔧Updates", url="https://t.me/TG_BotZ")]]
            keyboard += [[InlineKeyboardButton(text="🇮🇳 Language", callback_data="set_lang_"), 
                InlineKeyboardButton(text="❓Help", callback_data="help_back")]]
            keyboard += [[InlineKeyboardButton(text="🔌 Add me",url="http://t.me/Queen_isabellabot?startgroup=true")]

"""

    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
