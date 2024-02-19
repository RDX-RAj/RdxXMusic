from pyrogram.types import InlineKeyboardButton

import config
from RdxXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url="https://t.me/+PtOLQT04ocMzOTJl"),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_13"],
                url="https://t.me/+RObRa7kXPIJmMjU1"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"],
                url="https://t.me/+PtOLQT04ocMzOTJl"),
            InlineKeyboardButton(
                text=_["S_B_9"], 
                url="https://t.me/+RObRa7kXPIJmMjU1"),],[
            InlineKeyboardButton(text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"),],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id="6450320139"),
            InlineKeyboardButton(text=_["S_B_7"], url="https://t.me/+m4oVCt2zFhYyMTdl"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_10"], url="https://t.me/+okCO84m2hZxjYTE9"),
            InlineKeyboardButton(text=_["S_B_12"], url="https://www.youtube.com/channel/UCoOmopJ8YVYz9Lm8iHhNYMw"),
            InlineKeyboardButton(text=_["S_B_11"], url="https://t.me/+pAWm7GPhFYliOGI1"),
        ],
    ]
    return buttons
