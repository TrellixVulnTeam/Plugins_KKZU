import asyncio
import requests

from telethon import functions
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot, BotInlineDisabledError as noinline, YouBlockedUserError

from . import *

msg = f"""
**⚡ ʟɛɢɛռɖǟʀʏ ǟʄ ʋɨռƈɛռʐօɮօȶ⚡**
  •        [📑 Repo 📑](https://github.com/RealVinCenZo/VincenzoBot)
  •        [🚀 Deploy 🚀](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FRealVinCenZo%2FVincenzoBot&template=https%3A%2F%2Fgithub.com%2Frealvincenzo%2FvincenzoBot)
  •  ©️ {vincenzo_channel} ™
"""
botname = Config.BOT_USERNAME

@vincenzo_cmd(pattern="repo$")
async def repo(event):
    cids = await client_id(event)
    XD_RAJVEER, VINCENZO_USER, vincenzo_mention = cids[0], cids[1], cids[2]
    try:
        vincenzo = await event.client.inline_query(botname, "repo")
        await vincenzo[0].click(event.chat_id)
        if event.sender_id == XD_RAJVEER:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


@vincenzo_cmd(pattern="help$")
async def _(event):
    tgbotusername = Config.BOT_USERNAME
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "vincenzo_help")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except noinline:
            vincenzo = await eor(event, "**Inline Mode is disabled.** \n__Turning it on, please wait for a minute...__")
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await vincenzo.edit("Unblock @Botfather first.")
                await vincenzo.edit(f"**Turned On Inline Mode Successfully.** \n\nDo `{hl}help` again to get the help menu.")
            await bot.delete_messages(
                conv.chat_id, [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id]
            )
    else:
        await eor(event, "**⚠️ ERROR !!** \nPlease Re-Check BOT_TOKEN & BOT_USERNAME on Heroku.")


@vincenzo_cmd(pattern="plinfo(?:\s|$)([\s\S]*)")
async def vincenzobott(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, str(CMD_HELP[args]))
        else:
            await eod(event, "**⚠️ Error !** \nNeed a module name to show plugin info.")
    else:
        string = ""
        sayfa = [
            sorted(list(CMD_HELP))[i : i + 5]
            for i in range(0, len(sorted(list(CMD_HELP))), 5)
        ]

        for i in sayfa:
            string += f"`📌 `"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await eor(event, "Please Specify A Module Name Of Which You Want Info" + "\n\n" + string)
