from aiohttp import web, ClientSession

async def query_handler(request):
    data = await request.json()
    text = data['text']

    session = ClientSession()
    async with session.ws_connect('http://localhost:8080') as ws:
        await ws.send_str(text)
        msg = await ws.receive()
        return web.json_response({'response': msg.data})

app = web.Application()
app.add_routes([web.post('/query', query_handler)])

web.run_app(app, port=8000)