class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽.. 𝚃𝙷𝙴𝙽 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚂 ⚡🔥"""
    COMMANDS_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: 𝙴𝙼𝙸𝙻𝙸𝙰 𝙲𝙻𝙰𝚁𝙺𝙴</b>
<b>✯ 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁: <a href=https://t.me/Tanujairam>𝚃𝙰𝙽𝚄𝙹𝙰𝙸𝚁𝙰𝙼</a></b>
<b>✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</b>
<b>✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹</b>
<b>✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾-𝙳𝙱</b>
<b>✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄</b>"""
    FILE_TXT = """➤ 𝗙𝗶𝗹𝗲 𝘀𝘁𝗼𝗿𝗲 
𝙱𝚈 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚂𝚃𝙾𝚁𝙴 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝙼𝚈 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 𝙰𝙽𝙳 𝙸 𝚆𝙸𝙻𝙻 𝙶𝙸𝚅𝙴 𝚈𝙾𝚄 𝙰 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙻𝙸𝙽𝙺  𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙴 𝚂𝙰𝚅𝙴𝙳 𝙵𝙸𝙻𝙴𝚂.𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰 𝙿𝚄𝙱𝙻𝙸𝙲 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝙵𝙸𝙻𝚆 𝙻𝙸𝙽𝙺 𝙾𝙽𝙻𝚈 𝙾𝚁 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰  𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙾𝙽 𝚃𝙷𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝙵𝙸𝙻𝙴𝚂...

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
• /plink :- <b>𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝙼𝙴𝙳𝙸𝙰 𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝙽𝙺.</b>
• /pbatch :- <b>𝚄𝚂𝙴 𝚈𝙾𝚄𝚁 𝙼𝙴𝙳𝙸𝙰 𝙻𝙸𝙽𝙺 𝚆𝙸𝚃𝙷 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.</b>
• /batch :- <b>𝚃𝙾 𝙲𝚁𝙴𝙰𝚃𝙴 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙼𝚄𝙻𝚃𝙸𝙿𝙻𝙴 𝙵𝙸𝙻𝙴𝚂.</b>
"""
    WHOIS_TXT ="""➤ 𝗪𝗵𝗼 𝗶𝘀 
𝚃𝙾 𝙺𝙽𝙾𝚆 𝙰𝙻𝙻 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 𝙰𝙱𝙾𝚄𝚃 𝚃𝙷𝙴 𝚄𝚂𝙴𝚁

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
• /whois give a user full details"""
   
    FUN_TXT ="""➤ 𝗙𝘂𝗻𝘀 𝗺𝗼𝗱𝘂𝗹𝗲 
𝙹𝚄𝚂𝚃 𝚂𝙾𝙼𝙴 𝙺𝙸𝙽𝙳 𝙾𝙵 𝙵𝚄𝙽 𝚃𝙷𝙸𝙽𝙶𝚂

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
1. /dice - 𝚁𝙾𝙻𝙴 𝚃𝙷𝙴 𝙳𝙸𝙲𝙴 
2. /Throw 𝗈𝗋 /Dart - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙳𝙰𝚁𝚃 
3. /Runs - 𝚂𝙾𝙼𝙴 𝚁𝙰𝙽𝙳𝙾𝙼 𝙳𝙸𝙰𝙻𝙾𝙶𝚄𝙴𝚂 
4. /Goal or /Shoot - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙰 𝙶𝙾𝙰𝙻 𝙾𝚁 𝚂𝙷𝙾𝙾𝚃
5. /luck or /cownd - 𝚂𝙿𝙸𝙽 𝙰𝙽𝙳 𝚃𝚁𝚈 𝚈𝙾𝚄𝚁 𝙻𝚄𝙲𝙺
6. /throw_ball - Throw a ball
7. /basket_throw - Throw ball on basket"""
    MANUELFILTER_TXT = """➤ 𝗠𝗮𝗻𝘂𝗮𝗹 𝗳𝗶𝗹𝘁𝗲𝗿
Filter is the feature were users can set automated replies for a particular keyword and  will respond whenever a keyword is found the messagecan set automated replies for a particular keyword and  will respond whenever a keyword is found the message
<b>NOTE:</b>
1. Emilia should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    
    YTSEARCH_TXT = """➤ 𝗬𝗼𝘂𝘁𝘂𝗯𝗲 𝗩𝗶𝗱𝗲𝗼 𝗮𝗻𝗱 𝗮𝘂𝗱𝗶𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿 
𝚈𝚃 𝚅𝙸𝙳𝙴𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴, 𝙵𝙾𝚁 𝚃𝙷𝙾𝚂𝙴 𝚆𝙷𝙾 𝙻𝙾𝚅𝙴 𝙼𝚄𝚂𝙸𝙲. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙵𝙴𝙰𝚃𝚄𝙴 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾 𝚅𝙾𝙸𝙲𝙴 𝙰𝙽𝙳 𝙱𝙶𝙼 𝙻𝙸𝙺𝙴 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚆𝙸𝚃𝙷 𝚂𝚄𝙿𝙴𝚁 𝙵𝙰𝚂𝚃 𝚂𝙿𝙴𝙴𝙳.𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙾𝙽 𝙶𝚁𝙾𝚄𝙿𝚂../</b>
𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙳𝙸𝙽𝙶 𝚅𝙸𝙳𝙴𝙾𝚂 𝙰𝙽𝙳 𝚂𝙾𝙽𝙶𝚂 𝚆𝙸𝚃𝙷 𝙷𝙴𝙻𝙿 𝙾𝙵 𝚈𝙾𝚄𝚃𝚄𝙱𝙴</b>

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
• /mp3 for searching audio songs in youtube
• /mp4 for searching video songs in youtube
"""
    PIN_TXT ="""➤ 𝗣𝗶𝗻 𝗠𝗲𝘀𝘀𝗮𝗴𝗲
𝙿𝙸𝙽 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴..
𝙰𝙻𝙻 𝚃𝙷𝙴 𝙿𝙸𝙽 𝚁𝙴𝙻𝙰𝚃𝙴𝙳 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝙵𝙾𝚄𝙽𝙳 𝙷𝙴𝚁𝙴::</b>

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
• /pin :- 𝚃𝙾 𝙿𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂
• /unpin :- 𝚃𝙾 𝚄𝙽𝙿𝙸𝙽 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙴𝙽𝚃 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝙰𝙰𝙶𝙴"""
    
    PASTE_TXT = """➤ 𝗧𝗲𝘅𝘁 𝗽𝗮𝘀𝘁𝗲𝗿
Paste some texts or documents on a website!

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
• /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

• These commands works on both pm and group.
• These commands can be used by any group member."""
    
    TTS_TXT = """➤ 𝗧𝗲𝘅𝘁 𝘁𝗼 𝘀𝗽𝗲𝗲𝗰𝗵
𝚃𝚁𝙰𝙽𝚂𝙻𝙰𝚃𝙴 𝚃𝙴𝚇𝚃 𝚃𝙾 𝚂𝙿𝙴𝙴𝙲𝙷

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
• /tts <text> : convert text to speech

<b>NOTE:</b>

• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    
    PINGS_TXT ="""➤ 𝗣𝗶𝗻𝗴𝘀
𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝚈𝙾𝚄 𝙺𝙽𝙾𝚆𝚂 𝚈𝙾𝚄𝚁 𝙿𝙸𝙽𝙶 🚶🏼‍♂️

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
• /alive - To check you are alive.
• /commands - To get help.
• /ping - To get your ping..

Note
• This commands can be used in pms and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
    
    TELE_TXT = """ ➤ 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗽𝗵 𝘂𝗽𝗹𝗼𝗮𝗱𝗲𝗿
Do as you wish with telegra.ph module!

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
🤧 /telegraph - 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙿𝙸𝙲𝚃𝚄𝚁𝙴 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 𝚄𝙽𝙳𝙴𝚁 (5𝙼𝙱)

<b>NOTE:</b>

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""
    
    IP_TXT = """ ➤ 𝗜𝗽 𝗮𝗱𝗱𝗿𝗲𝘀𝘀 𝘁𝗿𝗮𝗰𝗸𝗲𝗿
    
    """
    JSON_TXT ="""➤ 𝗝𝘀𝗼𝗻
Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """➤ 𝗣𝘂𝗿𝗴𝗲 𝗼𝗿 𝗱𝗲𝗹𝗲𝘁𝗲
𝙳𝙴𝙻𝙴𝚃𝙴 𝙻𝙾𝚃 𝙾𝙵 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙵𝚁𝙾𝙼 𝙶𝚁𝙾𝚄𝙿! 
    
⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    
    BUTTON_TXT = """➤ 𝗕𝘂𝘁𝘁𝗼𝗻𝘀
Emilia Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Emilia supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/REX_BOTZ)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    
    AUTOFILTER_TXT = """➤ 𝗔𝘂𝘁𝗼𝗳𝗶𝗹𝘁𝗲𝗿
𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚃𝙾 𝚃𝚄𝚁𝙽 𝙾𝙵𝙵/𝙾𝙽 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙸𝙲𝙰𝙻𝙻𝚈 𝙵𝚁𝙾𝙼 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙶𝚁𝙾𝚄𝙿. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙴 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝚃𝙾 𝙾𝙽 𝙰𝙽𝙳 𝙾𝙵𝙵 𝚃𝙷𝙴 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿...

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
<b>›› /autofilter on - 𝙴𝙽𝙰𝙱𝙻𝙴 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>
<b>›› /autofilter off - 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>
<b>›› /set_template - 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙵𝙾𝚁 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b>›› /get_template - 𝙶𝙴𝚃 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙾𝙵 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>

"""
    CONNECTION_TXT = """➤ 𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽.
2. Send <code>/connect</code> for connecting me to ur PM

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    
    EXTRAMOD_TXT = """➤ 𝗘𝘅𝘁𝗿𝗮 𝗺𝗼𝗱𝘂𝗹𝗲𝘀
𝚃𝙷𝙴𝚂𝙴 𝙰𝚁𝙴 𝙴𝚇𝚃𝚁𝙰 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 𝙾𝙵 𝙴𝙼𝙸𝙻𝙸𝙰 𝙲𝙻𝙰𝚁𝙺𝙴

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    
    ADMIN_TXT = """➤ 𝗔𝗱𝗺𝗶𝗻𝘀

<b>NOTE:</b>
𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝙾𝙽𝙻𝚈 𝚆𝙾𝚁𝙺𝚂 𝙵𝙾𝚁 𝙼𝚈 𝙰𝙳𝙼𝙸𝙽𝚂

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban_user  - <code>to ban a user.</code>
• /unban_user  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    
    STATUS_TXT = """
█▀ ▀█▀ ▄▀█ ▀█▀ █▀
▄█ ░█░ █▀█ ░█░ ▄█
★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
  
    LOG_TEXT_G = """#𝗡𝗲𝘄_𝗴𝗿𝗼𝘂𝗽
    
<b>★ 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>★ 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>★ 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """𝗡𝗲𝘄_𝘂𝘀𝗲𝗿
    
<b>★ 𝐈𝐃 - <code>{}</code></b>
<b>★ 𝐍𝐚𝐦𝐞 - {}</b>
"""
    REPORT_TXT = """➤ 𝗥𝗲𝗽𝗼𝗿𝘁

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚛𝚎𝚙𝚘𝚛𝚝 𝚊 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚘𝚛 𝚊 𝚞𝚜𝚎𝚛 𝚝𝚘 𝚝𝚑𝚎 𝚊𝚍𝚖𝚒𝚗𝚜 𝚘𝚏 𝚝𝚑𝚎 𝚛𝚎𝚜𝚙𝚎𝚌𝚝𝚒𝚟𝚎 𝚐𝚛𝚘𝚞𝚙. 𝙳𝚘𝚗'𝚝 𝚖𝚒𝚜𝚞𝚜𝚎 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍.

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾)."""

    CORONA_TXT = """➤ 𝗖𝗼𝘃𝗶𝗱

𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>"""

    URLSHORT_TXT = """➤ 𝗨𝗿𝗹 𝘀𝗵𝗼𝗿𝘁𝗻𝗲𝗿

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/CPuvm126KPA</code>"""

    VIDEO_TXT ="""➤ 𝗬𝗼𝘂𝘁𝘂𝗯𝗲 𝘃𝗶𝗱𝗲𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝘁

• 𝘜𝘴𝘢𝘨𝘦
𝚈𝙾𝚄 𝙲𝙰𝙽 𝙳𝙾𝚆𝙽𝙻𝙾𝙳𝙴 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/9RVhig3kH3E)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/mp4 https://youtu.be/CPuvm126KPA</code>
<code>/video https://youtu.be/CPuvm126KPA</code>"""

    ZOMBIES_TXT = """➤ 𝗞𝗶𝗰𝗸 𝘂𝘀𝗲𝗿𝘀

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    IMAGE_TXT = """➤ 𝗜𝗺𝗮𝗴𝗲 𝗲𝗱𝗶𝘁

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚎𝚍𝚒𝚝 𝚒𝚖𝚊𝚐𝚎 𝚟𝚎𝚛𝚢 𝚎𝚊𝚜𝚒𝚕𝚢 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰 𝙸𝙼𝙰𝙶𝙴 𝚃𝙾 𝙴𝙳𝙸𝚃 ✨

 <b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂</b>


"""

    STICKER_TXT = """➤ 𝗦𝘁𝗶𝗰𝗸𝗲𝗿 𝗶𝗱
    𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.
• 𝐔𝐒𝐀𝐆𝐄
𝚃𝙾 𝙶𝙴𝚃 𝚂𝚃𝙸𝙲𝙺𝙴𝚁 𝙸𝙳
 
  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚

◉ 𝚁𝚎𝚙𝚕𝚊𝚢 𝚝𝚘 𝚜𝚝𝚒𝚌𝚔𝚎𝚛 [/stickerid]"""

    YTTHUMB_TXT = """➤ 𝗬𝗼𝘂𝘁𝘂𝗯𝗲 𝘁𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿
    𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻
    
⭕𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
𝘛𝘺𝘱𝘦 /ytthumb 𝘈𝘯𝘥 𝘝𝘪𝘥𝘦𝘰 𝘓𝘪𝘯𝘬

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦
<code>/ytthumb https://youtu.be/CPuvm126KPA</code>"""

    ABOOK_TXT = """➤ 𝗔𝘂𝗱𝗶𝗼𝗯𝗼𝗼𝗸

𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 ✯

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    GTRANS_TXT = """➤ 𝗚𝗼𝗼𝗴𝗹𝗲 𝘁𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗼𝗿

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚊 𝚝𝚎𝚡𝚝 𝚝𝚘 𝖺𝗇𝗒 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝. 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙 ✯

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    RESTRIC_TXT = """➤ 𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗶𝗼𝗻𝘀

𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚝𝚑𝚎𝚒𝚛 𝚐𝚛𝚘𝚞𝚙 𝚖𝚘𝚛𝚎 𝚎𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝𝚕𝚢.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""
    CREATOR_REQUIRED = """❗<b>𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝚃𝙾 𝙱𝙴 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿 𝙲𝚁𝙴𝙰𝚃𝙴𝚁 𝚃𝙾 𝙳𝙾 𝚃𝙷𝙰𝚃.</b>"""
      
    INPUT_REQUIRED = "❗ **𝙰𝚁𝙶𝚄𝙼𝙴𝙽𝚃𝚂 𝚁𝙴𝚀𝚄𝙸𝚁𝙴𝙳**"
      
    KICKED = """✔️ 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙺𝙸𝙲𝙺𝙴𝙳 {} 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝙰𝙲𝙲𝙾𝚁𝙳𝙸𝙽𝙶 𝚃𝙾 𝚃𝙷𝙴 𝙰𝚁𝙶𝚄𝙼𝙴𝙽𝚃𝚂 𝙿𝚁𝙾𝚅𝙸𝙳𝙴𝙳."""
      
    START_KICK = """💔 𝚁𝙴𝙼𝙾𝚅𝙸𝙽𝙶 𝙸𝙽𝙰𝙲𝚃𝙸𝚅𝙴 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝚃𝙷𝙸𝚂 𝙼𝙰𝚈 𝚃𝙰𝙺𝙴 𝙰 𝚆𝙷𝙸𝙻𝙴..."""
      
    ADMIN_REQUIRED = """❗<b>𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙸'𝙼 𝙽𝙾𝚃 𝙶𝙾𝙸𝙽𝙶 𝙰𝙽𝚈𝚆𝙷𝙴𝚁𝙴 𝙱𝙸𝙸..𝙰𝙳𝙳 𝙼𝙴 𝙰𝙶𝙰𝙸𝙽 𝚆𝙸𝚃𝙷 𝙰𝙻𝙻 𝙰𝙳𝙼𝙸𝙽 𝚁𝙸𝙶𝙷𝚃𝚂.</b>"""
      
    DKICK = """✔️  𝙺𝙸𝙲𝙺𝙴𝙳 {} 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙰𝙲𝙲𝙾𝚄𝙽𝚃𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈."""
      
    FETCHING_INFO = """<b>𝙽𝙾𝚆 𝙸 𝙲𝙰𝙽 𝙱𝙴𝙰𝚃 𝙴𝚅𝙴𝚁𝚈𝚃𝙷𝙸𝙽𝙶😈...</b>"""
      
    STATUS = """{}\n<b>𝙲𝙷𝙰𝚃 𝙼𝙴𝙼𝙱𝙴𝚁 𝚂𝚃𝙰𝚃𝚄𝚂</b>**\n\n```<i>𝚁𝙴𝙲𝙴𝙽𝚃𝙻𝚈``` - {}\n```𝚆𝙸𝚃𝙷𝙸𝙽 𝚆𝙴𝙰𝙺``` - {}\n```𝚆𝙸𝚃𝙷𝙸𝙽 𝙼𝙾𝙽𝚃𝙷``` - {}\n```𝙻𝙾𝙽𝙶 𝚃𝙸𝙼𝙴 𝙰𝙶𝙾``` - {}\n𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 - {}\n𝙱𝙾𝚃 - {}\n𝚄𝙽𝙲𝙰𝙲𝙷𝙴𝙳 - {}</i>
"""
