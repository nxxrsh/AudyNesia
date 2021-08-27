import asyncio
from collections import deque

from . import edit_or_reply, mention, udy

plugin_category = "utils"

@udy.cod_cmd(
    pattern="as$",
    command=("as", plugin_category),
    info={
        "header": "salam.",
        "usage": "{tr}as",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "as")
    await event.edit("yuuhuuuu")
    await asyncio.sleep(2)
    await event.edit("Assalamualaikum wr. wb.")

@udy.cod_cmd(
    pattern="ws$",
    command=("ws", plugin_category),
    info={
        "header": "answer the salam.",
        "usage": "{tr}ws",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "ws")
    await event.edit("huuyyyy")
    await asyncio.sleep(2)
    await event.edit("Waalaikum salam wr. wb.")
   
