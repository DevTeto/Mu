from pyrogram import filters
from YMusic import app
import config
from filters import command


START_COMMAND = ["الاوامر", "start"]

@app.on_message(command(START_COMMAND)
	)
async def _start(_, message):
	await message.reply_text("""🎤 ╖ أهـلا بك عزيزي 
 ⚙️╢ وظيفتي ميوزك المجموعات
 ✅╢ قم باضافه الحساب جهه اتصال
 🔘╢ ثم اضف الحساب إلى مجموعتك
 ⚡️╢ ارفعهُ » مشرف
 ⬆️╜ المـطور : @WZAERE""")
