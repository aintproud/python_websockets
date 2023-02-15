import asyncio
import websockets
import json


async def hello(websocket):
    async for message in websocket:
        message = json.loads(message)
        # print(message)

        if message['topic'] == 'name':
            await websocket.send(f'Hi, {message["text"]}!')
            print(">>> Write your name:")
            print(f'<<< {message["text"]}')
            print(f'>>> Hi {message["text"]}!')

        elif message['topic'] == 'propose':
            await websocket.send(f'You are the boss.{message["text"]},you decide what to do!')
            print(">>> Wanna go out?")
            print(f'<<< {message["vuv"]}')
            print(f'>>> You are the boss.{message["text"]},you decide what to do')

        elif message["topic"] == 'news':
            await websocket.send(f'I am your secretary, who will tell you what to do, if you need it, write. See you soon {message["text"]}!')
            print(">>> Want to know more?")
            print(f'<<< {message["drop"]}')
            print(f'>>> I am your secretary, who will tell you what to do, if you need it, write. See you soon {message["text"]}!')

async def main():
    async with websockets.serve(hello, "localhost", 8765, ping_timeout=None):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
