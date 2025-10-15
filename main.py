@client.event
async def on_message(message):
    # Only process messages in the target channel
    if message.channel.id != TARGET_CHANNEL_ID:
        return
    
    # Don't delete THIS bot's own messages, but delete other bots' messages
    if message.author.id == client.user.id:
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
