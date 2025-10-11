const { Client, GatewayIntentBits } = require('discord.js');

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
  ],
});

// Replace with your channel ID (just the numbers)
const TARGET_CHANNEL_ID = '1425176266293645363';
const DELETE_DELAY = 15000; // 15 seconds in milliseconds

client.on('ready', () => {
  console.log(`✅ Bot logged in as ${client.user.tag}`);
  console.log(`🗑️  Auto-deleting messages in channel ${TARGET_CHANNEL_ID} after 15 seconds`);
});

client.on('messageCreate', async (message) => {
  // Only process messages in the target channel
  if (message.channel.id !== TARGET_CHANNEL_ID) return;
  
  // Don't delete bot's own messages or messages that are already being deleted
  if (message.author.bot) return;

  try {
    // Wait 15 seconds then delete the message
    setTimeout(async () => {
      try {
        await message.delete();
        console.log(`🗑️  Deleted message from ${message.author.tag}`);
      } catch (error) {
        // Message might already be deleted or bot lacks permissions
        console.error('Error deleting message:', error.message);
      }
    }, DELETE_DELAY);
  } catch (error) {
    console.error('Error setting up deletion:', error);
  }
});

// Login with your bot token
client.login(process.env.DISCORD_BOT_TOKEN);
