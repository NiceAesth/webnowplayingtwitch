import asyncio
from twitchio.ext import commands
from classes import nowplaying

class MusicCog(commands.Cog):

    def __init__(self, bot: commands.Bot, socket_server: nowplaying.WebsocketServer) -> None:
        self.bot= bot
        self.socket_server = socket_server

    @commands.command(aliases=["nowplaying", "np"])
    async def song(self, ctx: commands.Context):
        await ctx.send(f"Currently Playing: {self.socket_server.get_current_data()}")

def prepare(bot: commands.Bot):
    socket_server = nowplaying.WebsocketServer()
    asyncio.get_event_loop().create_task(socket_server.main())
    bot.add_cog(MusicCog(bot, socket_server))
