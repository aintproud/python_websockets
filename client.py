import asyncio
import websockets
import json

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = json.dumps({"topic": 'name', "text": input("What's your name?")})
            print(message)
            await websocket.send(message)
            greeting = await websocket.recv()
            print(f"<<< {greeting}")
            
            message = json.dumps({"topic": 'propose', "text": input("Wanna go out?")})
            
            await websocket.send(message)
            print(f">>> {message}")

            greeting = await websocket.recv()
            print(f"<<< {greeting}")
            

if __name__ == "__main__":
    asyncio.run(hello())