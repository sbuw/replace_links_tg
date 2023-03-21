# ----------------------------------------

# WORKS ONLY FROM USER ACCOUNTS, THROUGH THE BOTS DOES NOT WORK
# WORKS ONLY FROM USER ACCOUNTS, THROUGH THE BOTS DOES NOT WORK
# WORKS ONLY FROM USER ACCOUNTS, THROUGH THE BOTS DOES NOT WORK

# ----------------------------------------

# ADS
# Channel about news from the front and the dark world --> t.me/ZPvoenkor
# Channel about news from the front and the dark world --> t.me/ZPvoenkor
# Channel about news from the front and the dark world --> t.me/ZPvoenkor
# ADS

# ----------------------------------------

from pyrogram import Client, enums
from time import sleep

api_id = 0123456 # my.telegram.org/
api_hash = "123345adfg2345" # my.telegram.org/

m_chat_id = -1234567890

old_link = ""
new_link = ""

app = Client("bot1", api_id=api_id, api_hash=api_hash)
app.start()

# entities
# caption_entities

for msg in app.get_chat_history(m_chat_id):
	
	try:
		if msg.text[-len(old_link):] == old_link : msg.edit_text(msg.text[:-(len(old_link)+1)] + f"**{new_link}**", parse_mode=enums.ParseMode.MARKDOWN)
	except:
		pass
	try:
		if msg.caption[-len(old_link):] == old_link: msg.edit_caption(msg.caption[:-(len(old_link)+1)] + f"**{new_link}**", parse_mode=enums.ParseMode.MARKDOWN)
	except:
		pass
	sleep(0.2)
	
app.stop()
