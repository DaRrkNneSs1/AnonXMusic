from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add Me To Your Group.",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="HELP",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="SETTINGS", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add Me To Your Group.",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="HELP", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="SUPPORT", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="OWNER", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="DeV ChanneL.", url=f"https://t.me/RQ_SF"
            )
        ],
     ]
    return buttons
