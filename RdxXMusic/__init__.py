from RdxXMusic.core.bot import Rdx
from RdxXMusic.core.dir import dirr
from RdxXMusic.core.git import git
from RdxXMusic.core.userbot import Userbot
from RdxXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Rdx()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
