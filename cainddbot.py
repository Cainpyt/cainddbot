from twitchio.ext import commands
from googletrans import Translator

translator = Translator()
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='91l7p7tn2pg6r1vczyugbc304baw5t', prefix='!', initial_channels=['caindd'])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return
        print(message.author.name + ':', message.content)
        # await self.handle_commands(message)
        if message.author.name == 'caindd':
            result = translator.translate(message.content, src='ru', dest='en')  # ctx.message.content
            result_for_bot = result.text
            print(result_for_bot)
        await self.handle_commands(message)

    async def event_translate(self, ctx: commands.Context, message):
        print('-----------------------------------')
        if message.author.name == 'caindd':
            result = translator.translate(message.content, src='ru', dest='en')  # ctx.message.content
            result_for_bot = result.text
            print('-----------------------------------')
            await message.send(result_for_bot)
        else:
            result = translator.translate(ctx.message.content, src='ru', dest='en')


    translator = Translator()

    @commands.command()
    async def t(self, ctx: commands.Context):

        if ctx.author.name == 'caindd':
            result = translator.translate(ctx.message.content, src='ru', dest='en') #ctx.message.content
            result_for_bot = result.text
            await ctx.send(result_for_bot[2:])
        #else:
            #await ctx.send(f'Nice try, {ctx.author.name}!')

bot = Bot()
bot.run()