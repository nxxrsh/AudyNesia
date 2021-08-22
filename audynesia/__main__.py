import sys

import audynesia
from audynesia import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import udy
from .utils import (
    add_bot_to_logger_group,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("AudyNesia")

print(audynesia.__copyright__)
print("Licensed under the terms of the " + audynesia.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("Starting Userbot")
    udy.loop.run_until_complete(setup_bot())
    LOGS.info("Telegram Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()


class AudyNesiaCheck:
    def __init__(self):
        self.sucess = True


AudyNesiacheck = AudyNesiaCheck()


async def startup_process():
    check = await ipchange()
    if check is not None:
        AudyNesiacheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("========================================")
    print("Okay, AudyNesia is Officially Working.!!!")
    print(
        f"Now type {cmdhr}alive to see message if udy is live\
        \nIf you need assistance."
    )
    print("========================================")
    print(audynesia.__copyright__)
    print("Licensed: " + audynesia.__license__)
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    AudyNesiacheck.sucess = True
    return


udy.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    udy.disconnect()
elif not AudyNesiacheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        udy.run_until_disconnected()
    except ConnectionError:
        pass
