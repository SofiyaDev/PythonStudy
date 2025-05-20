import asyncio
import websockets

async def websocket_handler(websocket):
    print("Клієнт підключився.")
    try:
        async for message in websocket:
            print(f"Отримано повідомлення: {message}")
            response = f"Ви сказали: {message}"
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        print("Клієнт відключився.")

async def main():
    async with websockets.serve(websocket_handler, "localhost", 8765):
        print("Сервер запущено на ws://localhost:8765")
        await asyncio.Future()  # нескінченне очікування

asyncio.run(main())

