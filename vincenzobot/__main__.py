import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

from vincenzobot import LOGS, bot, tbot
from vincenzobot.clients.session import Vincenzo, V2, V3, V4, V5
from vincenzobot.config import Config
from vincenzobot.utils import load_module
from vincenzobot.version import __vincenzo__ as vincenzover
hl = Config.HANDLER
HELL_PIC = "https://telegra.ph/file/2f6caa70b37d1e21a4f54.jpg"

# let's get the bot ready
async def h1(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"VINCENZOBOT_SESSION - {str(e)}")
        sys.exit()


# Multi-Client helper
async def Vincenzo_client(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


# Multi-Client Starter
def hells():
    failed = 0
    if Config.SESSION_2:
        LOGS.info("SESSION_2 detected! Starting 2nd Client.")
        try:
            V2.start()
            V2.loop.run_until_complete(vincenzo_client(V2))
        except:
            LOGS.info("SESSION_2 failed. Please Check Your String session.")
            failed += 1

    if Config.SESSION_3:
        LOGS.info("SESSION_3 detected! Starting 3rd Client.")
        try:
            V3.start()
            V3.loop.run_until_complete(vincenzo_client(V3))
        except:
            LOGS.info("SESSION_3 failed. Please Check Your String session.")
            failed += 1

    if Config.SESSION_4:
        LOGS.info("SESSION_4 detected! Starting 4th Client.")
        try:
            V4.start()
            V4.loop.run_until_complete(vincenzo_client(V4))
        except:
            LOGS.info("SESSION_4 failed. Please Check Your String session.")
            failed += 1

    if Config.SESSION_5:
        LOGS.info("SESSION_5 detected! Starting 5th Client.")
        try:
            V5.start()
            V5.loop.run_until_complete(vincenzo_client(V5))
        except:
            LOGS.info("SESSION_5 failed. Please Check Your String session.")
            failed += 1

    if not Config.SESSION_2:
        failed += 1
    if not Config.SESSION_3:
        failed += 1
    if not Config.SESSION_4:
        failed += 1
    if not Config.SESSION_5:
        failed += 1
    return failed


# vincenzo starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = tbot
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Starting VinCenZoBot 🔰")
            bot.loop.run_until_complete(h1(Config.BOT_USERNAME))
            failed_client = hells()
            global total
            total = 5 - failed_client
            LOGS.info("🔥 VinCenZoBot Startup Completed 🔥")
            LOGS.info(f"» Total Clients = {total} «")
        else:
            bot.start()
            failed_client = hells()
            total = 5 - failed_client
            LOGS.info(f"» Total Clients = {total} «")
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()


# imports plugins...
path = "vincenzobot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your VincenzoBot Is Now Working ⚡")
LOGS.info("Head to @RealVincenzo for Updates. Also join chat group to get help regarding to VincenzoBot.")
LOGS.info(f"» Total Clients = {total} «")

# that's life...
async def vincenzo_is_on():
    try:
        x = await bot.get_me()
        xid = telethon.utils.get_peer_id(x)
        send_to = Config.LOGGER_ID if Config.LOGGER_ID != 0 else xid
        await bot.send_file(
            send_to,
            HELL_PIC,
            caption=f"#START \n\n<b><i>Version :</b></i> <code>{hellver}</code> \n<b><i>Clients :</b></i> <code>{total}</code> \n\n<b><i>»» <u><a href='https://t.me/RealVincenzo'>The VinCenZoBot</a></u> ««</i></b>",
            parse_mode="HTML",
        )
    except Exception as e:
        LOGS.info(str(e))
# Join VincenzoBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@RealVincenzo"))
    except BaseException:
        pass
    try:
        if H2:
            await H2(JoinChannelRequest("@RealVincenzo"))
    except BaseException:
        pass
    try:
        if H3:
            await H3(JoinChannelRequest("@RealVincenzo"))
    except BaseException:
        pass
    try:
        if H4:
            await H4(JoinChannelRequest("@RealVincenzo"))
    except BaseException:
        pass
    try:
        if H5:
            await H5(JoinChannelRequest("@RealVincenzo"))
    except BaseException:
        pass
# Why not come here and chat??
    try:
        await bot(ImportChatInviteRequest('�MLq19ha27udhNDdl'))
    except BaseException:
        pass
    try:
        if H2:
            await H2(ImportChatInviteRequest('�MLq19ha27udhNDdl'))
    except BaseException:
        pass
    try:
        if H3:
            await H3(ImportChatInviteRequest('�MLq19ha27udhNDdl'))
    except BaseException:
        pass
    try:
        if H4:
            await H4(ImportChatInviteRequest('�MLq19ha27udhNDdl'))
    except BaseException:
        pass
    try:
        if H5:
            await H5(ImportChatInviteRequest('�MLq19ha27udhNDdl'))
    except BaseException:
        pass



bot.loop.create_task(vincenzo_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# vincenzobot
