import asyncio
import json
import websockets
import aiohttp
import threading

async def heartbeat(ws, interval):
    while True:
        await asyncio.sleep(interval)
        await ws.send(json.dumps({'op': 1, 'd': None}))

async def send_message(token, channel_id, content):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "content": content
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                print(f"Message sent: {content}")
            else:
                print(f"Failed to send message: {response.status}")

async def listen_to_gateway(token, gateway_url, on_message_callback):
    async with websockets.connect(gateway_url) as ws:
        identify_payload = {
            'op': 2,
            'd': {
                'token': token,
                'properties': {
                    '$os': 'linux',
                    '$browser': 'my_library',
                    '$device': 'my_library'
                }
            }
        }

        await ws.send(json.dumps(identify_payload))

        async for message in ws:
            event = json.loads(message)

            if event['op'] == 10:
                heartbeat_interval = event['d']['heartbeat_interval'] / 1000
                threading.Thread(target=asyncio.run, args=(heartbeat(ws, heartbeat_interval),)).start()

            if event['op'] == 0:
                if event['t'] == 'MESSAGE_CREATE':
                    await on_message_callback(event['d'])

def start_listener(token, gateway_url, on_message_callback):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(listen_to_gateway(token, gateway_url, on_message_callback)))