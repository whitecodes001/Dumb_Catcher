import asyncio
import json
import threading
import config.project_config
from backend import backend

async def handle_message(token, guild_id, message_data):
    author_id = message_data['author']['id']
    content = message_data['content']
    message_guild_id = message_data.get('guild_id')

    if message_guild_id == guild_id and message_data.get('guild_id') is not None:
        if author_id == backend.USER_ID and content.lower() == 'hello':
            channel_id = message_data['channel_id']
            await backend.send_message(token, channel_id, 'Hi')

def create_message_handler(token, guild_id):
    async def message_handler(message_data):
        await handle_message(token, guild_id, message_data)
    return message_handler

def start_bot():
    for account_config in backend.account_configs:
        token = account_config['TOKEN']
        guild_id = account_config['GUILD_ID']
        handler = create_message_handler(token, guild_id)
        threading.Thread(target=backend.start_listener, args=(token, backend.GATEWAY_URL, handler)).start()

def main():
    print("Starting the Discord bot...")
    start_bot()

if __name__ == "__main__":
    main()