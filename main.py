import discord
import asyncio
import os

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Configuration
TARGET_CHANNEL_ID = 1425176266293645363  # Your channel ID
DELETE_DELAY = 15  # seconds
WEBHOOK_ID = 1425176534926364923  # Your webhook ID to ignore

@client.event
async def on_ready():
    print(f'✅ Bot logged in as {client.user}')
    print(f'🗑️  Auto-deleting messages in channel {TARGET_CHANNEL_ID} after {DELETE_DELAY} seconds')
    print(f'📌 Ignoring messages from webhook {WEBHOOK_ID}')

@client.event
async def on_message(message):
    # Only process messages in the target channel
    if message.channel.id != TARGET_CHANNEL_ID:
        return
    
    # Don't delete THIS bot's own messages
    if message.author.id == client.user.id:
        return
    
    # Don't delete messages from your specific webhook
    if message.webhook_id == WEBHOOK_ID:
        return
    
    # Wait for the specified delay, then delete
    await asyncio.sleep(DELETE_DELAY)
    
    try:
        await message.delete()
        print(f'🗑️  Deleted message from {message.author.name}')
    except discord.errors.NotFound:
        print(f'⚠️  Message already deleted')
    except discord.errors.Forbidden:
        print(f'❌ Missing permissions to delete message')
    except Exception as e:
        print(f'❌ Error: {e}')

# Run the bot
client.run(os.environ.get('DISCORD_BOT_TOKEN'))
