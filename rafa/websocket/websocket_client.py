import asyncio
import aiohttp

async def main():

    session = aiohttp.ClientSession()

    async with session.ws_connect('http://localhost:8080') as ws:

        await ws.send_str('Hello, server!')
        msg = await ws.receive()
        print(msg.data)

        await ws.close()

    await session.close()

asyncio.run(main())