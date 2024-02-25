import asyncio
from pyrogram import Client, filters
from strings import get_string
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



REPLY_MESSAGE = "**صلي علي اشرف خلق الله 🥹✨**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
        ("الاوامر")
    ],
    
    [
        ("استوريهات")
    ],
    [
        ("العكس"),
        ("قران")
    ],
    [
        ("مطور السورس")
    ],
    [
        ("اقتباسات"),
        ("هيدرات")
    ],
    [
        ("احرف")
    ],
    [
        ("صوره"),
        ("انميي")
    ],
    [
        ("متحركه")
    ],
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("الالعاب")
    ],
    [
        ("نكته"),
        ("كتبات")
    ],
    [
        ("اذكار")
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
        ("يـوتيوب. 📽")
        
    ],
    [
        ("لو خيروك"),
        ("انصحني")
    ],
    [
        ("بوت حذف")
        
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
       ("انصحني")
        
    ],
    [
        ("اخفاء الازرار")
    ]
]

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("^اخفاء الازرار"))
async def down(client, message):
          m = await message.reply(" **- تم اخفاء الازرار بنجاح .\n\n- لاظهار كيب الارشادات /alpop   \n. 🕷**\n\n- لاظهار كيب الاعضاء والتسليه  /maro  \n. **", reply_markup= ReplyKeyboardRemove(selective=True))




@app.on_message(filters.regex("يـوتيوب. 📽"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/04b2f1f1c808dc49db35b.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ᯓ 𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 𖠛", url=f"https://t.me/UI_VM"),
            ]
         ]
     )
  )

