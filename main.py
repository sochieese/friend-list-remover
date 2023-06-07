import fortnitepy
import asyncio
import aioconsole
from fortnitepy.ext import commands    
bot = commands.Bot(
    command_prefix='!',
    auth=fortnitepy.AdvancedAuth(
        prompt_authorization_code=True,
        prompt_code_if_invalid=True,
        delete_existing_device_auths=True
    )
)
@bot.event
async def event_ready():
    print(f"program running as {bot.user.display_name}")
    input = await aioconsole.ainput("press enter y and enter if this is the right account: ")
    if input == "y":
        friends = len(bot.friends)
        print(f"{friends}/{friends}")
        await asyncio.sleep(5)
        for friend in bot.friends:
            await friend.remove()
            print(f"{len(bot.friends)}/{friends}")
        print("all friends removed if not run again")
        await bot.close()
    else:
        print("run again with the right account")
        await bot.close()
bot.run()