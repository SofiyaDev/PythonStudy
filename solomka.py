#\n \t
#sep, end
#+, -, /, *, **
#min, max, abs(виведення по модулю), pow(ступінь), round(округлення)
#input()
#return повертає все що завгодно
top = "лина"
for i in range(1 , 26):
    print(i, top)

    import asyncio
    from asyncio import start_server
    from http.client import responses

    import websockets


    async def websocket_hadler(websocket, path):
        while True:
            message = await websocket.recv()
            print(f"отримано повідомлення: {message}")

            response = f"ви сказали: {message}"
            await websocket.send(response)


    ws_server = websockets.serve(websocket_hadler, 'localhost', 8765)

    asyncio.get_event_loop().run_until_complete(ws_server)
    asyncio.get_event_loop().run_forever()