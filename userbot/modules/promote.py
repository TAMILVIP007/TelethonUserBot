"""Reply to a user to .promote them in the current chat"""
import logging
from datetime import datetime

from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from userbot import bot
from userbot.util import admin_cmd

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)


@bot.on(admin_cmd(pattern="promote ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    to_promote_id = None
    rights = ChatAdminRights(
        change_info=True,
        post_messages=True,
        edit_messages=True,
        delete_messages=True,
        ban_users=True,
        invite_users=True,
        pin_messages=True,
        add_admins=True,
    )
    input_str = event.pattern_match.group(1)
    if reply_msg_id := event.message.id:
        r_mesg = await event.get_reply_message()
        to_promote_id = r_mesg.sender_id
    elif input_str:
        to_promote_id = input_str
    try:
        await event.client(EditAdminRequest(event.chat_id, to_promote_id, rights, ""))
    except (Exception) as exc:
        await event.edit(str(exc))
    else:
        await event.edit("Successfully Promoted")


@bot.on(admin_cmd(pattern="prankpromote ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    to_promote_id = None
    rights = ChatAdminRights(
        post_messages=True
    )
    input_str = event.pattern_match.group(1)
    if reply_msg_id := event.message.id:
        r_mesg = await event.get_reply_message()
        to_promote_id = r_mesg.sender_id
    elif input_str:
        to_promote_id = input_str
    try:
        await event.client(EditAdminRequest(event.chat_id, to_promote_id, rights, ""))
    except (Exception) as exc:
        await event.edit(str(exc))
    else:
        await event.edit("Successfully Promoted")
