
import asyncio
import websockets
import json

async def hello(websocket):
    async for message in websocket:
        message = json.loads(message)
        print(message)
        
        if message['topic'] == 'name': await websocket.send(f'hi {message["text"]}')
        elif message['topic'] == 'propose': await websocket.send(f'you are the boss, {message["text"]} means {message["text"]}')


async def main():
    async with websockets.serve(hello, "localhost", 8765, ping_timeout=None):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())