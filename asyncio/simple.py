import asyncio
from datetime import datetime

def getTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

async def main():
    print('hello @' + getTime())
    await asyncio.sleep(1)
    print('world @' + getTime())

async def sec():
    print('sec @' + getTime())
    await asyncio.sleep(2)
    print('end @' + getTime())

async def allTasks():
    await asyncio.gather(main(), sec())

asyncio.run(allTasks())
