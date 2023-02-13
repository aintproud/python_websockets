import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            name = input("What's your name? ")

            await websocket.send(name)
            print(f">>> {name}")

            greeting = await websocket.recv()
            print(f"<<< {greeting}")
            
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(hello())