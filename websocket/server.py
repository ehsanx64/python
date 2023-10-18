#!/usr/bin/env python3

import asyncio
from websockets.server import serve

count = 0

async def echo(websocket):
    global count
    async for message in websocket:
        count = count + 1
        await websocket.send(str(count) + message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
