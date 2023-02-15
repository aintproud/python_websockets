import asyncio
import websockets
import json


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = {"topic": 'name', "text": input(">>> Write your name: ")}
            vsvod = json.dumps(message)
            await websocket.send(vsvod)
            v = message["text"]
            print("<<<",v)
            greeting = await websocket.recv()
            print(f">>> {greeting}")

            message = {"topic": 'propose', "text": v, "vuv": input(">>> Wanna go out?")}
            vsvod = json.dumps(message)
            print("<<<",message["vuv"])
            await websocket.send(vsvod)
            greeting = await websocket.recv()
            print(f">>> {greeting}")

            message = {"topic": 'news', "text": v, "drop": input(">>> Want to know more?")}
            vsvod = json.dumps(message)
            print("<<<", message["drop"])
            await websocket.send(vsvod)
            greeting = await websocket.recv()
            print(f">>> {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())
