
import asyncio
import websockets

async def hello(websocket):
    async for name in websocket:
        print(f"<<< {name}")

        greeting = f"Hello {name}!"

        await websocket.send(greeting)
        print(f">>> {greeting}")


async def main():
    async with websockets.serve(hello, "localhost", 8765, ping_timeout=None):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())