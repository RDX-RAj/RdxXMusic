from pyrogram import filters
from pyrogram.types import Message

from RdxXMusic import app
from RdxXMusic.core.call import Rdx

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Rdx.stop_stream_force(message.chat.id)
