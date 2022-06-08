# Backup & ForceSub
Automatically Forward files from groups to channel & Do force sub on members

## Variables
1. `API_ID` : Get from [my.telegram.org](https://my.telegram.org/)
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org)
3. `BOT_TOKEN` : Your telegram bot token from [@BotFather](https://t.me/BotFather)
4. `SESSION` : Generate from here [@String_Session_KDbot](t.me/String_Session_KDbot)
5. `GROUPS` : ID of Groups where the bot works (seperate by spaces)
6. `AUTO_DELETE` : Give True or False. If True, all messages in groups will be deleted after 10 minutes (not tested).
7. `DB_CHANNEL` : ID of the Backup Channel
8. `FSUB_CHANNEL` : ID of the ForceSub Channel
9. `CHANNEL_LINK` : Invite link of the ForceSub Channel

### Make sure:
- Bot is admin in Groups & ForceSub Channel
- Account used to create SESSION is member in Groups & admin in Backup Channel

## Deploy in Heroku
 [![Depoly](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/x-kunal/ForceSub-Backup)

### Credits
- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Kunal](https://t.me/kunal_nagar_01)
